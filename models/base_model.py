#!/usr/bin/python3

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Base class for all models in the application.

    Provides common functionalities like automatic ID generation,
    timestamps for creation and update, and methods for serializaion
    and deserializations.

    Attributes:
        id (str): Unique identifier for the object generated automatically
        created_at (datetime): Date and time of object creation.
        updated_at (datetime): Date and time of last object update.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer for the BaseModel class.
        """

        tformat = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tformat)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Defines string representation of the object

        Returns:
            str: A string representation of the object in the format:
                `[<class name>] (<id>) {<attributa name>=<attribute value>}`
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the `updated_at` attribute and saves the object to the storage
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the object to a dictionary representation.
        """
        empty_d = self.__dict__.copy()
        empty_d.update(__class__=self.__class__.__name__)
        empty_d["created_at"] = self.created_at.isoformat()
        empty_d["updated_at"] = self.updated_at.isoformat()
        return empty_d
