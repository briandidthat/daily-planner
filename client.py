from typing import List, Dict

from todoist_api_python.api_async import TodoistAPIAsync
from todoist_api_python.models import Task, Project

from exceptions import TodoistException


class TodoistClient:
    def __init__(self, api_key: str):
        self.api = TodoistAPIAsync(token=api_key)

    async def get_open_tasks(self, **kwargs) -> Dict[str, List[Task]]:
        """Fetch all of the open tasks"""
        try:
            tasks: List[Task] = await self.api.get_tasks(**kwargs)
            data: Dict[str, List[Task]] = dict()
            for task in tasks:
                project_id: str = task.project_id
                # if we already have this project as a key, append to list
                if project_id in data:
                    data[project_id].append(task)
                else:
                    data[project_id] = [task]
            return data
        except Exception as e:
            raise TodoistException(message=str(e), type=type(e).__name__)

    async def get_all_projects(self) -> List[Project]:
        """Fetch all of the projects in the workspace"""
        try:
            projects: List[Project] = await self.api.get_projects()
            return projects
        except Exception as e:
            raise TodoistException(message=str(e), type=type(e).__name__)