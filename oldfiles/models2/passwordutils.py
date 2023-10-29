#!/usr/bin/python3
""" Password Module """

import bcrypt


def hashpassword(password):
    """ hashes the input password """
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode('utf-8'), salt)

    return {"salt": salt, "password": hashedPassword}

def verifyUser(inputPassword, salt):
    """ Verify user using their entered password and corresponding salt from db """
    password = bcrypt.hashpw(inputPassword.encode('utf-8'), salt)
    return password
