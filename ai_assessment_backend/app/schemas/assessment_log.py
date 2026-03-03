from pydantic import BaseModel
from typing import Optional, Dict
from enum import Enum

class EventType(str, Enum):
    QUESTION_START = "QUESTION_START"
    QUESTION_SUBMIT = "QUESTION_SUBMIT"
    TIMER_EXPIRED = "TIMER_EXPIRED"
    FACE_DETECTED = "FACE_DETECTED"
    MULTIPLE_FACE = "MULTIPLE_FACE"
    FACE_NOT_VISIBLE = "FACE_NOT_VISIBLE"
    SUSPICIOUS_ACTIVITY = "SUSPICIOUS_ACTIVITY"
    
class LogEvent(BaseModel):
    candidate_id: str
    assessment_id: str
    question_id: Optional[str]
    event_type: str
    metadata: Optional[Dict]