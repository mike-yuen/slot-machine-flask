import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# REDIS_CONN_URL = os.environ.get("REDIS_CONN_URL")

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:123@localhost:5432/slot")


SEVEN_PROBABILITY = os.environ.get("SEVEN_PROBABILITY", 0.02)
#
# SOCKET_IO_EMITTER_KEY = os.environ.get("SOCKET_IO_EMITTER_KEY")
# REDIS_PUB_SUB_CREATE_USER_CHAT_APP = os.environ.get(
#     "REDIS_PUB_SUB_CREATE_USER_CHAT_APP"
# )


JWT_PUBLIC_KEY_PATH = os.environ.get("JWT_PUBLIC_KEY_PATH", default="jwt_api_key.pub")
JWT_PUBLIC_KEY = open(JWT_PUBLIC_KEY_PATH).read()
