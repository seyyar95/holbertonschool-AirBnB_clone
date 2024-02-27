#!/usr/bin/python3

from datetime import datetime
import uuid
from __init__ import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        tformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tformat)
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        empty_d = self.__dict__.copy()
        empty_d.update(__class__=self.__class__.__name__)
        empty_d["created_at"] = self.created_at.isoformat()
        empty_d["updated_at"] = self.updated_at.isoformat()
        return empty_d
