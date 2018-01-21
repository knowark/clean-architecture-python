from abc import ABC, abstractmethod
from taskit.application.models.task import Task


class TaskRepository(ABC):
    @abstractmethod
    def add(self, task: Task) -> bool:
        "Add method to be implemented."

    @abstractmethod
    def get(self, uid: str) -> Task:
        "Get method to be implemented."
