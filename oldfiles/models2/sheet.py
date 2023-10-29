#!/usr/bin/python3
""" Sheet Module """

from basemodel import BaseModel
from datetime import datetime
from user import User
from board import Board


class Sheet:
    """ Sheet Model """

    def __init__(self, **kwargs):
        basedata = BaseModel()
        self.id = basedata.to_dict()["id"]
        self.createdAt = basedata.to_dict()["createdAt"]
        self.updatedAt = basedata.to_dict()["updatedAt"]
        
        for k, v in kwargs.items():
            if k == "boardID":
                self.boardID = v
            if k == "data":
                self.data = v
            if k == "createdBy":
                self.createdBy = v

    def update(self, **kwargs):
        """ Updates the instance with new updated data """
        for k, v in kwargs.items():
            if k == "data":
                self.data = v
        self.updatedAt = str(datetime.now())

    def to_dict(self):
        """ Returns a dictionary representation of the instance """
        return self.__dict__


userdata = {"firstName": "Bismark", "lastName": "Arthur", "email": "bismarkarthur@gmail.com", "bio": "I live in Accra, Ghana"}
user = User(**userdata)
userID = {"createdBy": user.to_dict()["id"]}

board = Board(**userID)

sheetdata = {"boardID": board.to_dict()["id"],
             "createdBy": board.to_dict()["createdBy"],
             "data": "Ikjdnjknjdbjd dbjkdndjnkdkjkd njkjknlkndnkdlnklndlnlkndjkbvhskjnllsnlnlksklsnld ljd"
             }
sheet = Sheet(**sheetdata)
print("USER: ", user.to_dict())
print("\n", "BOARD", board.to_dict())
print("\n", "SHEET: ", sheet.to_dict())
