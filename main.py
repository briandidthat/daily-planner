import os
import asyncio

from pprint import pprint
from typing import Dict, List

from client import TodoistClient

TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = TodoistClient(api_key=TODOIST_API_KEY)

if __name__ == "__main__":

    tasks = asyncio.run(client.get_open_tasks())
    for project, tasks in tasks.items():
        for task in tasks:
            pprint(task)
