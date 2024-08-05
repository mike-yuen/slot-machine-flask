### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

server.venv: ## Create a virtual environment
	python -m venv venv && .\venv\Scripts\activate

server.install: ## Install server with its dependencies
	pip install -r requirements-dev.txt --upgrade

server.start: ## Start server in its docker container
	python src/server.py

server.upgrade: ## Upgrade pip dependencies
	bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"
