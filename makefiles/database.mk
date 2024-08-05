### DATABASE
# ¯¯¯¯¯¯¯¯


database.connect: ## Connect to database
	db psql -Upostgres

database.migrate: ## Create alembic migration file
	python src/manage.py db migrate

database.upgrade: ## Upgrade to latest migration
	python src/manage.py db upgrade

database.downgrade: ## Downgrade latest migration
	python src/manage.py db downgrade
