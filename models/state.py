#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state or province within a country in the application.
    Inherits from the `BaseModel`.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
