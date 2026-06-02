import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from app.dependency import get_broker_consumer, get_tasks_repository
from app.tasks.handlers import router as task_router
from app.tasks.repository import TaskRepository
from app.users.auth.handlers import router as auth_router
from app.users.user_profile.handlers import router as user_router


async def _consume(broker_consumer):
    async for message in broker_consumer.consume_callback_message():
        print(f"Email callback: {message}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    broker_consumer = await get_broker_consumer()
    task = asyncio.create_task(_consume(broker_consumer))
    yield
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)


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
