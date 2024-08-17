#Chat FastAPI app

## Prerequisites:
- Python 3.7
- Redis
- FastAPI

## Setup Configuration Files

```bash

# Edit DATABASE_URL in ./config/.env
DATABASE_URL=postgres://goldfish:123456@postgres:5432/goldfish
```

## Install Pre-commit Hooks
Pre-commit hooks are executed as soon as you commit code to reformat and validate PEP8 standard

```bash
pre-commit install

# Test hooks
pre-commit run --all-files
```

## virtualenv

```bash
# 1. Create virtual env
python3 -m venv virtualenv
. virtualenv/bin/activate

# 2. Install dependency
pip install -r requirements.txt

# 3. Migrate database
alembic upgrade head

# 4. Start Apps
uvicorn main:app --reload
```


## Usage with model

- Add model code in `models.py` file.
- Import new model added in `db/base.py` to declare.
- Run `alembic revision --autogenerate -m "Migration content"` to make migrations.
- Run `alembic upgrade head` to migrate.


## Run celery
Run command
```bash
celery -A app.tasks.celery worker --loglevel=info
```
In window should run with `gevent`


# Initial data
- Run `initial_data.py` to create message type.
- Run `create_materialized_view.py` to create channel index view.
- For create user, there two ways to implement:
  - Run `redis_pub_sub.py` at the start apps
  - From django core app call `/chat/users/` api to create.

