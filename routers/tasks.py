from typing import Dict, List

from fastapi import APIRouter, HTTPException, status, Request

from client import todoist_client
from exceptions import TodoistException

from todoist_api_python.models import Task, Project

router = APIRouter()


@router.get(
    "/tasks", status_code=status.HTTP_200_OK, response_model=Dict[str, List[Task]]
)
async def get_open_tasks(request: Request) -> Dict[str, List[Task]]:
    try:
        response = await todoist_client.get_open_tasks(**request.query_params)
        return response
    except TodoistException as e:
        raise HTTPException(status_code=400, detail=e.serialize())


@router.get("/projects", status_code=status.HTTP_200_OK, response_model=List[Project])
async def get_all_pojects():
    try:
        response = await todoist_client.get_all_projects()
        return response
    except TodoistException as e:
        raise HTTPException(status_code=400, detail=e.serialize())
