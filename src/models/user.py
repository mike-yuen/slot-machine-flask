"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.mysql import INTEGER


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "user"

    email = db.Column(db.String(500), unique=True, nullable=True)
    name = db.Column(db.String(64), nullable=True)
    picture = db.Column(db.String(255), nullable=True)
    # chip = db.Column(INTEGER(unsigned=True), nullable=True)

    def __init__(self, email, name, picture, chip):
        """ Create a new User """
        self.email = email
        self.name = name
        self.picture = picture
        self.chip = chip
