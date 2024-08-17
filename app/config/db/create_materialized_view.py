import logging

from app.config.db.session import engine
from sqlalchemy.ext.declarative import DeferredReflection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def handle():
    print("=========START=========")
    with engine.connect() as con:
        con.execute(
            "CREATE MATERIALIZED VIEW IF NOT EXISTS channel_index AS ( \
            SELECT c.id, c.id as channel_id,\
                p.id as participant_id, \
                c.name, p.user_id, \
                (case when p.user_id = c.friend_id then c.owner_id when p.user_id = c.owner_id and c.type='ONE-ONE' \
                then c.friend_id end) as friend_id, \
                c.type, \
                c.avatar, \
                c.avatar_thumb, \
                c.last_message_time, \
                c.last_message, \
                c.is_removed, \
                setweight(to_tsvector(coalesce(c.name, '')), 'A') || \
                coalesce((SELECT setweight(to_tsvector(coalesce(u.display_name, '')), 'B') \
                FROM participant p2 \
                INNER JOIN chatuser u ON p2.user_id = u.id AND p2.channel_id = c.id \
                WHERE c.type = 'ONE-ONE' \
                    AND u.id != p.user_id \
                    AND p2.is_removed='0' \
                LIMIT 1),'') as document \
            FROM channel c \
            INNER JOIN participant p ON c.id = p.channel_id\
            WHERE c.is_removed='0' AND p.is_removed='0')"
        )
        con.execute(
            "CREATE INDEX IF NOT EXISTS idx_fts_chat_channel ON channel_index USING GIN(document)"
        )
        con.execute(
            "CREATE INDEX IF NOT EXISTS idx_fts_chat_channel_user_id ON channel_index(id)"
        )
        con.execute(
            "CREATE UNIQUE INDEX IF NOT EXISTS idx_fts_participant_id ON channel_index(participant_id)"
        )
        print("=========END=========")
        DeferredReflection.prepare(con)


def main() -> None:
    logger.info("Creating ")
    handle()
    logger.info("ted")


if __name__ == "__main__":
    main()
