#!/usr/bin/python3
""" User Module """

from sqlalchemy import String, Column, DateTime, ForeignKey
from basemodel import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
#from user import User


class User(Base):
    """ User Model """
    
    __tablename__ = "users"

    id = Column(String(255), primary_key=True)
    username = Column(String(255), unique=True, nullable=True)
    firstName = Column(String(255), nullable=False)
    lastName = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    createdAt = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())

    boards = relationship("Board", back_populates="createdByID")
