from sqlalchemy import Column, Integer, String, Float
from database import Base

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    caste = Column(String)
    course = Column(String)
    income = Column(Float)

class Scholarship(Base):
    __tablename__ = "scholarships"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    eligible_castes = Column(String)   # store as CSV for now
    eligible_courses = Column(String)  # store as CSV
    amount = Column(Float)
    deadline = Column(String)

    
