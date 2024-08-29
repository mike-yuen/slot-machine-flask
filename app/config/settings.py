import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "..//..//.env")
load_dotenv(dotenv_path)
DEFAULT_DB = "postgresql://postgres:123@localhost:5432/defaultdb"

APPLICATION_PORT = os.environ.get("APPLICATION_PORT", 8000)
APPLICATION_POSTGRES_URL = os.environ.get("APPLICATION_POSTGRES_URL", DEFAULT_DB)
JWT_ACCESS_TOKEN_SECRET = os.environ.get("JWT_ACCESS_TOKEN_SECRET", "")
JWT_REFRESH_TOKEN_SECRET = os.environ.get("JWT_REFRESH_TOKEN_SECRET", "")
SEVEN_PROBABILITY = os.environ.get("SEVEN_PROBABILITY", 0.02)
