#!/usr/bin/python3
""" User Module """

from basemodel import BaseModel
from passwordutils import hashpassword, verifyUser
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey



class User:
    """ User Model """

    def __init__(self, **kwargs):
        """ Initializes an instance of the user model """
        if not isinstance(kwargs, dict):
            return

        basedata = BaseModel()

        self.id = basedata.to_dict()["id"]
        self.createdAt = basedata.to_dict()["createdAt"]
        self.updatedAt = basedata.to_dict()["updatedAt"]

        for k, v in kwargs.items():
            if k == "firstName":
                self.firstName = v
            if k == "lastName":
                self.lastName = v
            if k == "email":
                self.email = v
            if k == "bio":
                self.bio = v
            if k == "password":
                p = hashpassword(v)
                self.password = p["password"]
                self.salt = p["salt"]

    def to_dict(self):
        """ Returns  dictionary representation of the instance """
        return self.__dict__

    def update(self, **kwargs):
        """ Updates the instance with new values """
        for k, v in kwargs.items():
            if k == "firstName": 
                self.firstName = v
            if k == "lastName": 
                self.lastName = v
            if k == "email": 
                self.email = v
            if k == "bio": 
                self.bio = v
            if k == "password":
                p = hashpassword(v)
                self.password = p["password"]
                self.salt = p["salt"]
