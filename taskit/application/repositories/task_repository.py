from abc import ABC, abstractmethod
from typing import Dict, Optional
from taskit.application.models.task import Task
from taskit.application.repositories.errors import EntityNotFoundError


class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> None:
        "Add method to be implemented."

    @abstractmethod
    def get(self, uid: str) -> Task:
        "Get method to be implemented."

    @abstractmethod
    def update(self, task: Task) -> None:
        "Update method to be implemented."

    @abstractmethod
    def delete(self, task: Task) -> None:
        "Delete method to be implemented."


class MemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self.tasks = {}  # type: Dict[str, Task]
        self.sequence = 1

    def add(self, task: Task) -> None:
        task.uid = task.uid or ("T-" + str(self.sequence))
        self.tasks[task.uid] = task
        self.sequence += 1

    def get(self, uid: str) -> Task:
        task = self.tasks.get(uid)
        if not task:
            raise EntityNotFoundError("Task not found.")
        return task

    def update(self, task: Task) -> None:
        uid = task.uid
        old_task = self.tasks.get(uid)
        if not old_task:
            raise EntityNotFoundError("Task not found.")
        self.tasks[uid] = task

    def delete(self, task: Task) -> None:
        uid = task.uid
        old_task = self.tasks.get(uid)
        if not old_task:
            raise EntityNotFoundError("Task not found.")
        del self.tasks[uid]

    def load(self, tasks_dict: Dict[str, Task]) -> None:
        self.tasks = tasks_dict
