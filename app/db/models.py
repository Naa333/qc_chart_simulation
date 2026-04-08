from sqlalchemy import Column, Float, Integer, String

from app.db.database import Base


class ResultRecord(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    sample_id = Column(String, nullable=False, index=True)
    value = Column(Float, nullable=False)
