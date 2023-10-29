#!/usr/bin/python3
"""DB Storage"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from basemodel import Base

"""Instantiate a DBStorage object"""
BOARDLY_MYSQL_USER = getenv('BOARDLY_MYSQL_USER')
BOARDLY_MYSQL_PWD = getenv('BOARDLY_MYSQL_PWD')
BOARDLY_MYSQL_HOST = getenv('BOARDLY_MYSQL_HOST')
BOARDLY_MYSQL_DB = getenv('BOARDLY_MYSQL_DB')
BOARDLY_ENV = getenv('BOARDLY_ENV')
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                              format(BOARDLY_MYSQL_USER,
                                     BOARDLY_MYSQL_PWD,
                                     BOARDLY_MYSQL_HOST,
                                     BOARDLY_MYSQL_DB))

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
