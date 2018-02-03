from typing import Dict
from taskit.application.models.project import Project
from taskit.application.repositories.project_repository import ProjectRepository
from taskit.application.repositories.task_repository import TaskRepository


class AdminCoordinator:
    def __init__(self, project_repository: ProjectRepository,
                 task_repository: TaskRepository) -> None:
        self.task_repository = task_repository
        self.project_repository = project_repository

    def create_project(self, project_dict: Dict[str, any]):
        # Intantiate a Task object
        project = Project(**project_dict)

        # Add the new task to the task repository
        self.project_repository.add(project)
