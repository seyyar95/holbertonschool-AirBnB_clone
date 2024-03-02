#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city within the application.
    Inherits from the `BaseModel` class

    Attributes:
        state_id (str): the ID of the state to wich the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
