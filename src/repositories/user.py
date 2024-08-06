""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(id):
        """ Query a user by id """
        return User.query.filter_by(id=id).one()
    
    @staticmethod
    def get_user_by_email(email):
        """ Query a user by email """
        return User.query.filter_by(email=email).one()

    def update_chip(self, id, chip):
        """ Update user's chip """
        user = self.get(id)
        user.chip = chip

        return user.save()

