from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task API")

tasks = {
    1: {"id": 1, "title": "Read about testing", "completed": False},
    2: {"id": 2, "title": "Write an API test", "completed": False},
}


@app.get("/tasks")
def list_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
