from app.config.database import engine


def handle():
    print("=========START=========")
    with engine.connect() as con:
        con.execute("DROP MATERIALIZED VIEW IF EXISTS channel_index")
    print("=========END=========")


def main() -> None:
    handle()


if __name__ == "__main__":
    main()
