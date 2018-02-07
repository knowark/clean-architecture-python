from typing import Dict
from taskit.application.models.project import Project
from taskit.application.models.task import Task
from taskit.application.repositories.project_repository import ProjectRepository
from taskit.application.repositories.task_repository import TaskRepository


class AdminCoordinator:
    def __init__(self, project_repository: ProjectRepository,
                 task_repository: TaskRepository) -> None:
        self.task_repository = task_repository
        self.project_repository = project_repository

    def create_project(self, project_dict: Dict[str, any]):
        project = Project(**project_dict)
        self.project_repository.add(project)

    def update_project(self, project_dict: Dict[str, any]):
        uid = project_dict.get('uid')
        old_project = self.project_repository.get(uid)
        old_project_dict = vars(old_project)
        old_project_dict.update(project_dict)
        new_project = Project(**old_project_dict)
        self.project_repository.update(new_project)

    def delete_project(self, uid: str):
        project = self.project_repository.get(uid)
        self.project_repository.delete(project)

    def update_task(self, task_dict: Dict[str, any]):
        uid = task_dict.get('uid')
        old_task = self.task_repository.get(uid)
        old_task_dict = vars(old_task)
        old_task_dict.update(task_dict)
        new_task = Task(**old_task_dict)
        self.task_repository.update(new_task)

    def delete_task(self, uid: str):
        task = self.task_repository.get(uid)
        self.task_repository.delete(task)
