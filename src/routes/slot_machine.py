"""
Defines the blueprint for the slot machine
"""
from flask import Blueprint
from flask_restful import Api

from resources import SlotMachineResource

SLOT_MACHINE_BLUEPRINT = Blueprint("slot-machine", __name__)
Api(SLOT_MACHINE_BLUEPRINT).add_resource(
    SlotMachineResource, "/slot-machine"
)
