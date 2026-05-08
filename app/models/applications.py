from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False)
    status = Column(String(50), nullable=False)  # e.g., "Applied", "Interviewing", "Offer", "Rejected"
    user_id = Column(Integer, nullable=False)  # Foreign key to User.id