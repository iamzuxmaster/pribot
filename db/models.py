from sqlalchemy import Column, String, DateTime, Integer, Boolean,ForeignKey
from datetime import datetime
from dispatcher import Base, Session, engine, create_db

session_db = Session(bind=engine)

class Admin(Base): 
    __tablename__ = "admin"
    id = Column(Integer(), primary_key=True)
    telegram_id = Column(String(80), nullable=False)
    fullname=  Column(String(80), nullable=False)
    phone = Column(Integer(), nullable=False)
    date_created = Column(DateTime(), default=datetime.utcnow)


class Users(Base): 
    __tablename__ = 'Users'
    id = Column(Integer(), primary_key=True)
    telegram_id = Column(String(80), nullable=False)
    fullname=  Column(String(80), nullable=False)
    username = Column(String(80), nullable=False, unique=True)
    phone = Column(Integer(), nullable=False)
    request_group = Column(String(80), nullable=False)
    verified = Column(Boolean(), default=False)
    date_created = Column(DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return f"< User: {self.fullname}, ID: {self.telegram_id}/>"


class Groups(Base): 
    __tablename__ = 'Groups'
    id = Column(Integer(), primary_key=True)
    telegram_id = Column(String(), nullable=True)
    title = Column(String(80), nullable=False, unique=True)


class Messages(Base): 
    __tablename__ = "Messages"
    id = Column(Integer(), primary_key=True)
    from_admin = Column(Integer(), ForeignKey('admin.id'), )
    all = Column(Boolean(), nullable=True)
    title = Column(String(80), nullable=False)
    description = Column(String(300), nullable=True)
    date_created  = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<Messages: {self.title}, date: {self.date_created}"