#!/user/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents a single amenity available at a place.

    Attributes:
        name (str): The name of the amenity (e.g., "Wi-Fi", "Kitchen").
    """
    name = ""
