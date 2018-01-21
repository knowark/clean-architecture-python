from abc import ABC, abstractmethod
from typing import Dict
from taskit.application.models.task import Task


class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> bool:
        "Add method to be implemented."

    @abstractmethod
    def get(self, uid: str) -> Task:
        "Get method to be implemented."


class MemoryTaskRepository(TaskRepository):
    def __init__(self) -> None:
        self.tasks = {}  # type: Dict[str, Task]

    def add(self, task: Task) -> bool:
        "Add method to be implemented."

    def get(self, uid: str) -> Task:
        "Get method to be implemented."

    def load(self, tasks_dict: Dict[str, Task]) -> None:
        self.tasks = tasks_dict
