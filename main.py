from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class TodoItem(BaseModel):
    task: str

@app.post("/todos")
async def create_todo(item: TodoItem):
    new_todo = {"id": str(uuid.uuid4()), "task": item.task}
    return new_todo
