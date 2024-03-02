#!/user/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place on the platform.
    Inherits from the `BaseModel`.

    Attributes:
        place_id (str): The ID of the place the review is associated with
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
