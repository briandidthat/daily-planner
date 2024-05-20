from typing import List

from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.models import Task, Project

from exceptions import TodoistException


class TodoistClient:
    def __init__(self, api_key: str):
        self.api = TodoistAPIAsync(token=api_key)

    async def get_open_tasks(self, **kwargs) -> List[Task]:
        """Fetch all of the open tasks"""
        try:
            tasks = await self.api.get_tasks(**kwargs)
            return tasks
        except Exception as e:
            raise TodoistException(e)

    async def get_all_projects(self) -> List[Project]:
        """Fetch all of the projects in the workspace"""
        try:
            projects = await self.get_all_projects()
            return projects
        except Exception as e:
            raise TodoistException(e)
