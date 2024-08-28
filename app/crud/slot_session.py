import random

from app.config import settings


class SlotSessionCrud:
    def run_slot_session(self):
        # check if total profit is lowest now
        # run slot session
        numbers = [0, 1, 2, 3, 4, 5, 6, 7]
        probabilities = [0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

        result = random.choices(numbers, weights=probabilities, k=3)

        # save slot session with user
        # return slot session
        print(result)
        return result
