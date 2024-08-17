import re

from app.config import settings


def is_absolute_url(url: str) -> bool:
    if re.match(r"^https?://", url):
        return True
    return False


def get_absolute_url(url: str) -> str:
    if is_absolute_url(url):
        return url

    base_url = str(settings.BASE_URL).rstrip("/")
    return f'{base_url}/{url.lstrip("/")}'


def get_media_url(file_path: str) -> str:
    if is_absolute_url(file_path):
        return file_path
    url = f"{settings.MEDIA_URL}{file_path}"
    return get_absolute_url(url)
