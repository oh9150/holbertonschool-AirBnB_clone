#!/usr/bin/python3
"""Defines a class BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """Instantiates a BaseClass object"""
        self.id = str(uuid4())
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
            return
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """Returns the string representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Updates the 'updated_at' public instance attribute to the current
        datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of
        the current instance"""
        ret_dict = self.__dict__.copy()
        ret_dict["created_at"] = self.created_at.isoformat()
        ret_dict["updated_at"] = self.updated_at.isoformat()
        ret_dict["__class__"] = str(type(self))
        return ret_dict
