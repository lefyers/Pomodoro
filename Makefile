ENV_FILE ?= .local.env

run: #make run ENV_FILE=.local.env
	poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 4 --env-file $(ENV_FILE)

# poetry run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload --env-file $(ENV_FILE)

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


#taskkill /F /IM python.exe
#poetry env remove pomodoro-poetry-mraVSAeY-py3.14   Чтобы не плодить лишние venv, можно удалить WSL-овский если он не нужен:


#для запуска воркеров
#cd /mnt/f/project/pomodoro-analytics
#poetry run celery -A worker.celery worker --loglevel=info

#pytest tests/integration/auth/test_auth_service.py::test_google_auth__login_not_exist_user

#celery --broker=redis://localhost:6379/0 flower --host=127.0.0.1 --port=5555

