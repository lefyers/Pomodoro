ENV_FILE ?= .local.env

run: #make run ENV_FILE=.local.env
	poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload --env-file $(ENV_FILE)

install: #make install LIBRARY=pydantic
	poetry add $(LIBRARY)

uninstall:
	poetry remove $(LIBRARY)

update:
	poetry update $(LIBRARY)

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
	alembic upgrade head





