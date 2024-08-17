import logging

from app import choices, models
from app.config.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    # initial message type
    types = [
        choices.MESSAGE_TYPE_TEXT,
        choices.MESSAGE_TYPE_IMAGE,
        choices.MESSAGE_TYPE_VIDEO,
        choices.MESSAGE_TYPE_FILE,
        choices.MESSAGE_TYPE_SYSTEM,
    ]
    type_create = []
    for i in types:
        type_create.append(
            models.MessageType(name=i, key=i)  # type:ignore
        )
    db.bulk_save_objects(type_create)
    db.commit()


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
