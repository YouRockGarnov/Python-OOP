from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    duration: int


@app.post("/task")
async def create_task(task: Task):
    # TODO: Implement this function
    raise NotImplementedError


@app.get("/task/{task_id}")
async def get_task_status(task_id: str):
    # TODO: Implement this function
    raise NotImplementedError
