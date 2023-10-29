#!/usr/bin/python3
""" Board Module """

from sqlalchemy import String, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from basemodel import Base
from sqlalchemy.sql import func
#from user import User


class Board(Base):
    """  Board Model """

    __tablename__ = "boards"

    id = Column(String(255), primary_key=True)
    createdByID = Column(String(255), ForeignKey('users.id'), nullable=False)
    createdAt = Column(DateTime, nullable=False, server_default=func.now())
    updatedAt = Column(DateTime, nullable=False, server_default=func.now())

    createdby = relationship("User", back_populates="boards")
    sheets = relationship("Sheet", back_populates="board")
