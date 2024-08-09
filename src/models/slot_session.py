"""
Define the SlotSession model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.dialects.postgresql import ARRAY

class SlotSession(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The SlotSession model """

    __tablename__ = "slot_session"

    bet = db.Column(INTEGER(unsigned=True), nullable=True)
    result = db.Column(ARRAY(db.String), nullable=True)
    change = db.Column(db.Integer, nullable=True)

    def __init__(self, bet, result, change):
        """ Create a new SlotSession """
        self.bet = bet
        self.result = result
        self.change = change
