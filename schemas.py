from typing import List, Any
from pydantic import BaseModel


class TaskResponse(BaseModel):
    assignee_id: str
    assigner_id: str
    comment_count: int
    is_completed: bool
    content: str
    created_at: str
    creator_id: str
    description: str
    id: str
    labels: List[str]
    order: int
    parent_id: str
    priority: int
    project_id: str
    section_id: str
    url: str
    duration: Any


"""
Task(assignee_id=None,
     assigner_id=None,
     comment_count=1,
     is_completed=False,
     content='Clean the house',
     created_at='2024-05-26T19:08:05.622183Z',
     creator_id='49291530',
     description='**Current streak:** 0 days',
     due=Due(date='2024-06-01',
             is_recurring=True,
             string='every saturday',
             datetime=None,
             timezone=None),
     id='8024316994',
     labels=['mom'],
     order=1,
     parent_id=None,
     priority=1,
     project_id='2333406869',
     section_id='156008782',
     url='https://todoist.com/app/task/8024316994',
     duration=None,
     sync_id=None)
"""
