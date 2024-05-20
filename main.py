import os
import asyncio

from client import TodoistClient

TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

client = TodoistClient(api_key=TODOIST_API_KEY)

if __name__ == "__main__":
    print(asyncio.run(client.get_all_projects()))