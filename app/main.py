# import asyncio
# from app.dependency import get_broker_consumer
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from app.dependency import  get_tasks_repository
from app.tasks.handlers import router as task_router
from app.tasks.repository import TaskRepository
from app.users.auth.handlers import router as auth_router
from app.users.user_profile.handlers import router as user_router
import sentry_sdk

sentry_sdk.init(
    dsn="https://a61b03b1eb6278d762383658ad9615c8@o4511496344698880.ingest.us.sentry.io/4511496355381248",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)


async def _consume(broker_consumer):
    async for message in broker_consumer.consume_callback_message():
        print(f"Email callback: {message}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # broker_consumer = await get_broker_consumer()
    # task = asyncio.create_task(_consume(broker_consumer))
    yield
    # task.cancel()
    # await asyncio.gather(task, return_exceptions=True)


app = FastAPI(lifespan=lifespan)

app.include_router(task_router)
app.include_router(auth_router)
app.include_router(user_router)


@app.get("/app/ping")
async def ping_app():
    return {"text": "app is working"}


@app.get("/db/ping")
async def ping_db(task_repository: TaskRepository = Depends(get_tasks_repository)):
    await task_repository.ping_db()


@app.get("/sentry-debug")
async def trigger_error():
    1 / 0
