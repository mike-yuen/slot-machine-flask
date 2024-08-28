import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "..//..//.env")
load_dotenv(dotenv_path)

APPLICATION_POSTGRES_URL = os.environ.get(
    "APPLICATION_POSTGRES_URL", "postgresql://postgres:123@localhost:5432/slot"
)
SEVEN_PROBABILITY = os.environ.get("SEVEN_PROBABILITY", 0.02)
# JWT_PUBLIC_KEY_PATH = os.environ.get("JWT_PUBLIC_KEY_PATH", default="jwt_api_key.pub")
# JWT_PUBLIC_KEY = open(JWT_PUBLIC_KEY_PATH).read()
