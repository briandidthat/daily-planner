from typing import Dict, List

from fastapi import APIRouter, HTTPException, status

from client import todoist_client
from exceptions import TodoistException

from todoist_api_python.models import Task

router = APIRouter()


@router.get(
    "/tasks", status_code=status.HTTP_200_OK, response_model=Dict[str, List[Task]]
)
async def get_open_tasks() -> Dict[str, List[Task]]:
    try:
        response = await todoist_client.get_open_tasks()
        return response
    except TodoistException as e:
        raise HTTPException(status_code=400, detail=e.serialize())
