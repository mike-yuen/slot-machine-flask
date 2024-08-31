import random

from app.config.settings import MAX_BET, MIN_BET, PROBABILITIES, REEL, Symbol
from app.models.user import User
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


class SlotSessionCrud:
    def _define_score(self, result):
        score = 0

        if result == [Symbol.SEVEN, Symbol.SEVEN, Symbol.SEVEN]:
            score = 400
        elif result == [Symbol.COIN, Symbol.COIN, Symbol.COIN]:
            score = 200
        elif result == [Symbol.BAR, Symbol.BAR, Symbol.BAR]:
            score = 100
        elif result == [Symbol.ORANGE, Symbol.ORANGE, Symbol.ORANGE]:
            score = 50
        elif result == [Symbol.CHERRY, Symbol.CHERRY, Symbol.CHERRY]:
            score = 18
        elif result == [Symbol.CHERRY, Symbol.CHERRY, Symbol.SEVEN]:
            score = 18
        elif result == [Symbol.DISLIKE, Symbol.DISLIKE, Symbol.DISLIKE]:
            score = 14
        elif result == [Symbol.DISLIKE, Symbol.DISLIKE, Symbol.SEVEN]:
            score = 14
        elif result == [Symbol.HORSESHOE, Symbol.HORSESHOE, Symbol.HORSESHOE]:
            score = 10
        elif result == [Symbol.HORSESHOE, Symbol.HORSESHOE, Symbol.SEVEN]:
            score = 10
        elif result[:2] == [Symbol.DIAMOND, Symbol.DIAMOND]:
            score = 5
        elif result[:2] == [Symbol.ORANGE, Symbol.ORANGE]:
            score = 5
        elif result[:2] == [Symbol.SEVEN, Symbol.SEVEN]:
            score = 2
        elif result[:1] == [Symbol.DIAMOND]:
            score = 2
        elif result[:1] == [Symbol.BAR]:
            score = 2
        elif result[:1] == [Symbol.SEVEN]:
            score = 1

        return score

    def randomize_result(self, current_user: User, bet: int):
        if current_user.chip < MIN_BET:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Insufficient chips",
            )

        if bet < MIN_BET or bet > MAX_BET:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail="Invalid bet",
            )

        response = {"bet": bet, "result": [], "score": 0}

        # run randomized algorithm
        result = sum(
            [random.choices(REEL, weights=weights) for weights in PROBABILITIES], []
        )
        score = self._define_score(result)
        response["result"] = result
        response["score"] = score

        # save slot session with user
        win = score * bet
        change = win - bet
        response["change"] = change

        return response
