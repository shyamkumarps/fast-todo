from fastapi import FastAPI
from pydantic import BaseModel
 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://127.0.0.1:8000","https://fast-api-steel.vercel.app/","https://next-todo-eta-ten.vercel.app/"],  # Replace with your front-end origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define the TodoItem model with additional fields
class TodoItem(BaseModel):
    title: str
    description: str
    status: str
    userId: str

# Define the endpoint to create a new todo item
@app.post("/todos")
async def create_todo(item: TodoItem):
    # Create a new todo item with a unique ID
    new_todo = {
        
        "userId": item.userId,
        "title": item.title,
        "description": item.description,
        "status": item.status
    }
    return new_todo

# To run the application, use: uvicorn filename:app --reload
