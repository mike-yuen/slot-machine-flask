import os
from enum import Enum
from os.path import dirname, join

from dotenv import load_dotenv

# .env

dotenv_path = join(dirname(__file__), "..//..//.env")
load_dotenv(dotenv_path)
DEFAULT_DB = "postgresql://postgres:123@localhost:5432/defaultdb"

APPLICATION_PORT = os.environ.get("APPLICATION_PORT", 8000)
APPLICATION_POSTGRES_URL = os.environ.get("APPLICATION_POSTGRES_URL", DEFAULT_DB)
JWT_ACCESS_TOKEN_SECRET = os.environ.get("JWT_ACCESS_TOKEN_SECRET", "")
JWT_REFRESH_TOKEN_SECRET = os.environ.get("JWT_REFRESH_TOKEN_SECRET", "")

# game
MIN_BET = 10
MAX_BET = 100


class Symbol(Enum):
    DISLIKE = 0
    CHERRY = 1
    HORSESHOE = 2
    ORANGE = 3
    BAR = 4
    COIN = 5
    SEVEN = 6
    DIAMOND = 7


# ⚽  5   1   5  // dislike
# 🏈  1	  8	  1  // cherry
# ⚾  4   1   10 // horseshoe
# 🎾  4	  2	  1  // orange
# 🏉  2	  1	  1  // bar
# 🎱  1   1	  1  // coin
# 🏀  1	  1	  1  // seven
# 🏐  2	  5	  0  // diamond

REEL = [
    Symbol.DISLIKE,
    Symbol.CHERRY,
    Symbol.HORSESHOE,
    Symbol.ORANGE,
    Symbol.BAR,
    Symbol.COIN,
    Symbol.SEVEN,
    Symbol.DIAMOND,
]

PROBABILITIES = [
    [5 / 20, 1 / 20, 4 / 20, 4 / 20, 2 / 20, 1 / 20, 1 / 20, 2 / 20],
    [1 / 20, 8 / 20, 1 / 20, 2 / 20, 1 / 20, 1 / 20, 1 / 20, 5 / 20],
    [5 / 20, 1 / 20, 10 / 20, 1 / 20, 1 / 20, 1 / 20, 1 / 20, 0],
]
