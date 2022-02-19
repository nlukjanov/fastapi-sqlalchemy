from datetime import datetime
from http.client import HTTPException
from uuid import UUID, uuid4

from data_access.models import Task, User
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from api.schemas import (CreateTaskSchema, GetTaskSchema, ListTasksSchema,
                         Status)
from api.server import server, session_maker

TODO = []


@server.get('/todo', response_model=ListTasksSchema)
def get_tasks(request: Request):
    user_id = request.state.user_id
    with session_maker() as session:
        tasks = [task.dict() for task in session.query(
            User).filter(User.id == user_id).first().tasks]
    return {'tasks': tasks}


@server.post('/todo', response_model=GetTaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(request: Request, payload: CreateTaskSchema):
    with session_maker() as session:
        task = Task(
            created=datetime.utcnow(),
            updated=datetime.utcnow(),
            priority=payload.priority.value,
            status=payload.status.value,
            task=payload.task,
            user_id=request.state.user_id
        )
        session.add(task)
        session.commit()
        task = task.dict()
    return task


@server.get('/todo/{task_id}', response_model=GetTaskSchema)
def get_task(task_id: UUID):
    for task in TODO:
        if task['id'] == task_id:
            return task
    raise HTTPException(
        status_code=404, detail=f'Task with ID {task_id} was not found')


@server.put('/todo/{task_id}', response_model=GetTaskSchema)
def update_task(task_id: UUID, payload: CreateTaskSchema):
    for task in TODO:
        if task['id'] == task_id:
            task.update(payload.dict())
            task['status'] = task['status'].value
            task['priority'] = task['priority'].value
            return task
    raise HTTPException(
        status_code=404, detail=f'Task with ID {task_id} was not found')


@server.delete('/todo/{task_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_task(task_id: UUID):
    for index, task in enumerate(TODO):
        if task['id'] == task_id:
            TODO.pop(index)
            return
    raise HTTPException(
        status_code=404, detail=f'Task with ID {task_id} was not found')
