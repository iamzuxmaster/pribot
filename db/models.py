from sqlalchemy import Column, String, DateTime, Integer, Boolean,ForeignKey
from datetime import datetime
from .dispatcher import Base, Session, engine

session_db = Session(bind=engine)

class User(Base): 
    __tablename__ = 'User'
    id = Column(Integer(), primary_key=True)
    telegram_id = Column(String(80), nullable=False)
    fullname=  Column(String(80), nullable=True)
    username = Column(String(80), nullable=True, unique=True)
    phone = Column(Integer(), nullable=True)
    ban = Column(Boolean(), default=False)
    date_created = Column(DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return f"< User: {self.fullname}, ID: {self.telegram_id}/>"

class Admin(Base): 
    __tablename__ = 'Admin'
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("User.id"), nullable=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"< User: {self.fullname}, ID: {self.telegram_id}/>"