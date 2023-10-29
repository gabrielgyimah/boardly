#!/usr/bin/python3
""" Board Module """

from datetime import datetime
from basemodel import BaseModel
from user import User


class Board:
    """  Board Model """

    def __init__(self, **kwargs):
        """ Initializes an instance of the board model """
        basedata = BaseModel()
        
        self.id = basedata.to_dict()["id"]
        self.createdAt = basedata.to_dict()["createdAt"]
        self.updatedAt = basedata.to_dict()["updatedAt"]

        for k, v in kwargs.items():
            if k == "createdBy":
                self.createdBy = v

    def update(self):
        """ Updates the instance """
        self.updatedAt = self.updatedAt = str(datetime.now())

    def to_dict(self):
        """ Returns a dictionary representation of the instance """
        return self.__dict__
