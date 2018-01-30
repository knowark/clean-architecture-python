from abc import ABC, abstractmethod
from typing import Dict, Optional
from taskit.application.models.project import Project
from taskit.application.repositories.errors import EntityNotFoundError


class ProjectRepository(ABC):
    @abstractmethod
    def add(self, project: Project) -> None:
        "Add method to be implemented."

    @abstractmethod
    def get(self, uid: str) -> Project:
        "Get method to be implemented."

    @abstractmethod
    def update(self, project: Project) -> None:
        "Update method to be implemented."

    @abstractmethod
    def delete(self, project: Project) -> None:
        "Delete method to be implemented."


class MemoryProjectRepository(ProjectRepository):
    def __init__(self) -> None:
        self.projects = {}  # type: Dict[str, Project]
        self.sequence = 1

    def add(self, project: Project) -> None:
        project.uid = project.uid or ("P-" + str(self.sequence))
        self.projects[project.uid] = project
        self.sequence += 1

    def get(self, uid: str) -> Project:
        project = self.projects.get(uid)
        if not project:
            raise EntityNotFoundError("Project not found.")
        return project

    def update(self, project: Project) -> None:
        uid = project.uid
        old_project = self.projects.get(uid)
        if not old_project:
            raise EntityNotFoundError("Project not found.")
        self.projects[uid] = project

    def delete(self, project: Project) -> None:
        uid = project.uid
        old_project = self.projects.get(uid)
        if not old_project:
            raise EntityNotFoundError("Project not found.")
        del self.projects[uid]

    def load(self, projects_dict: Dict[str, Project]) -> None:
        self.projects = projects_dict
