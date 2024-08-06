"""
Define the REST verbs relative to the slot machine
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import UserRepository
from util import parse_params


class SlotMachineResource(Resource):
    """ Verbs relative to the slot machine """

    @staticmethod
    @parse_params(
        Argument("bet", location="json", required=True, help="The bet amount of the user.")
    )
    @swag_from("../swagger/slot_machine/POST.yml")
    def post(bet):
        """ Spin the slot machine based on the bet amount """
        repository = UserRepository()
        user = repository.get(1)
        return jsonify({"user": user.json})
