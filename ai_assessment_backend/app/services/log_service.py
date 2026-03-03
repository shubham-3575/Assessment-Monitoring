from sqlalchemy.orm import Session
from app.models.assessment_log import AssessmentLog

def create_log(db: Session, log_data, ip_address, user_agent):
    new_log = AssessmentLog(
        candidate_id=log_data.candidate_id,
        assessment_id=log_data.assessment_id,
        question_id=log_data.question_id,
        event_type=log_data.event_type,
        event_metadata=log_data.metadata,  # 🔥 changed
        ip_address=ip_address,
        user_agent=user_agent
    )

    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log