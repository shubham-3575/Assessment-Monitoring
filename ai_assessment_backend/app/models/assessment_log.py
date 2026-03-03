import uuid
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from app.core.database import Base

class AssessmentLog(Base):
    __tablename__ = "assessment_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    candidate_id = Column(String, nullable=False)
    assessment_id = Column(String, nullable=False)
    question_id = Column(String)
    event_type = Column(String, nullable=False)
    event_timestamp = Column(TIMESTAMP, server_default=func.now())

    # 🔥 FIXED HERE
    event_metadata = Column("metadata", JSONB)

    ip_address = Column(String)
    user_agent = Column(String)