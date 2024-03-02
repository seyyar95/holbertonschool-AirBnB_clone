#!/user/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user of the platform.
    Inherits from the `BaseModel`.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password (hashed and stored securely).
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
