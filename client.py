import os
from enum import Enum
from typing import List, Dict, Any

from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.models import Task, Project

from exceptions import TodoistException
from logger import todist_logger


class TodoistClient:

    def __init__(self, api_key: str):
        self.api = TodoistAPIAsync(token=api_key)

    async def get_all_projects(self) -> List[Project]:
        """Fetch all of the projects in the workspace"""
        try:
            projects: List[Project] = await self.api.get_projects()
            todist_logger.info("Fetched projects", extra=dict(projects=projects))
            return projects
        except Exception as e:
            raise TodoistException(message=str(e), type=type(e).__name__)

    async def get_open_tasks(self, **kwargs) -> Dict[str, List[Task]]:
        """Fetch all of the open tasks"""
        try:
            tasks: List[Task] = await self.api.get_tasks(**kwargs)
            todist_logger.info("Fetched projects", extra=dict(tasks=tasks))
            response: Dict[str, List[Task]] = dict()
            for task in tasks:
                project_id: str = task.project_id
                # if we already have this project as a key, append to list
                if project_id in response:
                    response[project_id].append(task)
                else:
                    response[project_id] = [task]
            return response
        except Exception as e:
            raise TodoistException(message=str(e), type=type(e).__name__)

    async def get_all_sections(self, **kwargs):
        """Fetch all sections"""
        try:
            sections = await self.api.get_sections(**kwargs)
            return sections
        except Exception as e:
            exception = TodoistException(message=str(e), type=type(e).__name__)
            todist_logger.error(
                "Unexpected throwable encountered",
            )
            raise exception


TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")
todoist_client = TodoistClient(api_key=TODOIST_API_KEY)
