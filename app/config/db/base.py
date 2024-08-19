# Import all the models, so that Base has them before being
# imported by Alembic
from app.config.db.base_class import Base  # noqa
from app.models.user import User
from app.models.slot_session import SlotSession
