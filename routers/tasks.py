from typing import Dict, List, Any

from fastapi import APIRouter, HTTPException, status, Request

from client import todoist_client
from exceptions import TodoistException

from todoist_api_python.models import Task, Project, Section

router = APIRouter()


def validate_params(params: Dict[str, Any]):
    available_params = dict(
        project_id="project_id", section_id="section_id", label="label", filter="filter"
    )

    for param in params.keys():
        if not available_params.get(param, None):
            raise ValueError(f"Invalid param. {param}")

        return True


@router.get("/projects", status_code=status.HTTP_200_OK, response_model=List[Project])
async def get_all_pojects():
    try:
        response = await todoist_client.get_all_projects()
        return response
    except TodoistException as e:
        raise HTTPException(status_code=400, detail=e.serialize())


@router.get(
    "/tasks", status_code=status.HTTP_200_OK, response_model=Dict[str, List[Task]]
)
async def get_open_tasks(request: Request):
    try:
        validate_params(request.query_params)
        response = await todoist_client.get_open_tasks(**request.query_params)
        return response
    except ValueError as v:
        raise HTTPException(status_code=422, detail=str(v))
    except TodoistException as e:
        raise HTTPException(status_code=400, detail=e.serialize())


@router.get("/sections", status_code=status.HTTP_200_OK, response_model=List[Section])
async def get_all_sections(request: Request):
    try:
        validate_params(request.query_params)
        response = await todoist_client.get_all_sections(**request.query_params)
        return response
    except ValueError as v:
        raise HTTPException(status_code=422, detail=str(e))
    except TodoistException as e:
        raise HTTPException(status_code=400, detail=e.serialize())
