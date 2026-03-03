from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from typing import Optional
from app.core.database import get_db
from app.schemas.assessment_log import LogEvent,EventType
from app.services.log_service import create_log
from app.models.assessment_log import AssessmentLog
from sqlalchemy import func
from datetime import datetime

router = APIRouter()

@router.post("/log-event")
async def log_event(log: LogEvent, request: Request, db: Session = Depends(get_db)):
    create_log(
        db=db,
        log_data=log,
        ip_address=request.client.host,
        user_agent=request.headers.get("user-agent")
    )
    return {"message": "Log stored successfully"}

# ✅ GET — Fetch Logs with Filtering
@router.get("/logs/{assessment_id}")
def get_logs(
    assessment_id: str,
    candidate_id: Optional[str] = None,
    event_type: Optional[EventType] = None,
    db: Session = Depends(get_db)
):
    query = db.query(AssessmentLog)\
              .filter(AssessmentLog.assessment_id == assessment_id)

    if candidate_id:
        query = query.filter(AssessmentLog.candidate_id == candidate_id)

    if event_type:
        query = query.filter(AssessmentLog.event_type == event_type)

    logs = query.order_by(AssessmentLog.event_timestamp.asc()).all()

    return logs

@router.get("/logs/{assessment_id}/summary")
def get_log_summary(assessment_id: str, db: Session = Depends(get_db)):
    
    total_logs = db.query(func.count(AssessmentLog.id))\
                   .filter(AssessmentLog.assessment_id == assessment_id)\
                   .scalar()

    suspicious_events = db.query(func.count(AssessmentLog.id))\
        .filter(
            AssessmentLog.assessment_id == assessment_id,
            AssessmentLog.event_type == EventType.SUSPICIOUS_ACTIVITY
        ).scalar()

    multiple_face_events = db.query(func.count(AssessmentLog.id))\
        .filter(
            AssessmentLog.assessment_id == assessment_id,
            AssessmentLog.event_type == EventType.MULTIPLE_FACE
        ).scalar()

    face_not_visible_events = db.query(func.count(AssessmentLog.id))\
        .filter(
            AssessmentLog.assessment_id == assessment_id,
            AssessmentLog.event_type == EventType.FACE_NOT_VISIBLE
        ).scalar()

    question_submissions = db.query(func.count(AssessmentLog.id))\
        .filter(
            AssessmentLog.assessment_id == assessment_id,
            AssessmentLog.event_type == EventType.QUESTION_SUBMIT
        ).scalar()

    return {
        "total_logs": total_logs,
        "suspicious_events": suspicious_events,
        "multiple_face_events": multiple_face_events,
        "face_not_visible_events": face_not_visible_events,
        "question_submissions": question_submissions
    }

@router.get("/logs/{assessment_id}")
def get_logs(
    assessment_id: str,
    candidate_id: str | None = None,
    event_type: EventType | None = None,
    start_time: datetime | None = None,
    end_time: datetime | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(AssessmentLog)\
              .filter(AssessmentLog.assessment_id == assessment_id)

    if candidate_id:
        query = query.filter(AssessmentLog.candidate_id == candidate_id)

    if event_type:
        query = query.filter(AssessmentLog.event_type == event_type)

    if start_time:
        query = query.filter(AssessmentLog.event_timestamp >= start_time)

    if end_time:
        query = query.filter(AssessmentLog.event_timestamp <= end_time)

    logs = query.order_by(AssessmentLog.event_timestamp.asc()).all()

    return logs