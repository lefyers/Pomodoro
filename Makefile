ENV_FILE ?= .local.env

run: #make run ENV_FILE=.local.env
	poetry run uvicorn main:app --host 127.0.0.1 --port 8000 --reload --env-file $(ENV_FILE)

add: #make add LIBRARY=pydantic
	poetry add $(LIBRARY)

uninstall:
	poetry remove $(LIBRARY)

update:
	poetry update $(LIBRARY)

migrate-create:
	alembic revision --autogenerate -m $(MIGRATION)

migrate-apply:
	alembic upgrade head





