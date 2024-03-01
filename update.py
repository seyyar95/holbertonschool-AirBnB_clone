#!/usr/bin/python3


from models.user import User
from models import storage

b = User()
b.email = ""
print(storage.all())
