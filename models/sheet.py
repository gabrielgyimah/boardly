#!/usr/bin/python3
""" Board Module """

from sqlalchemy import String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from basemodel import Base
from sqlalchemy.sql import func
#from user import User
#from board import Board


class Sheet(Base):
    """ Defines the structure of the sheets table """
    __tablename__ = "sheets"

    id = Column(String(255), primary_key=True)
    data = Column(String(10000), nullable=False)
    boardID = Column(String(255), ForeignKey("boards.id"), nullable=False)
    createdByID = Column(String(255), ForeignKey("users.id"), nullable=False)
    createdAt = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())

    createdby = relationship("User")
    board = relationship("Board")
