# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.slot_session import SlotSession
from app.models.user import User
