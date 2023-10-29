#!/usr/bin/python3
""" Basemodel Module """

import uuid
from datetime import datetime
import sqlalchemy
from storage import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey

Base = declarative_base()


class BaseModel(Base):
    """ Creates the basic object structure of a model """
    id = Column(String (255) primary_key=True)
    createdAt = Column(DateTime, default=datetime.utcnow)
    updatedAt = Column(DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        """Initializes a model"""
        if Kwargs:
            for k, v in kwargs.items():
                if k not "__class__":
                    setattr(self, k, v)
            if kwargs.get("createdAt", None) and type(self.createdAt) is str:
                self.createdAt = datetime.strptime(kwargs["createdAt"], time)
            else:
                self.createdAt = datetime.utcnow()
            if kwargs.get("updatedAt", None) and type(self.updatedAt) is str:
                self.updatedAt = datetime.strptime(kwargs["updatedAt"], time)
            else:
                self.updatedAt = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.createdAt = str(datetime.now())
            self.updatedAt = str(datetime.now())

    def to_dict(self):
        """ Converts the instance into a dictionary """
        return self.__dict__

    def save(self):
        """ Saves an instance to the database """
        obj = storage.new()
        storage.save()

    def delete(self):
        """ Deletes and instance from the database """
        storage.delete(self)
