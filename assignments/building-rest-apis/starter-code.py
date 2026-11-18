from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


# The tasks are stored in memory and reset when the application restarts.
tasks: dict[int, dict] = {}
next_task_id = 1


@app.get("/tasks")
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", status_code=201)
def create_task(task_input: TaskInput):
    # TODO: assign an ID, save the task, and return it
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: return the task or raise HTTPException with status code 404
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_input: TaskInput):
    # TODO: replace the task data or raise HTTPException with status code 404
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    # TODO: remove the task or raise HTTPException with status code 404
    pass
