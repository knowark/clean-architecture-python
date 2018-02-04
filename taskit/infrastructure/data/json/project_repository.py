from taskit.application.models.project import Project
from taskit.application.repositories.project_repository import ProjectRepository


class JsonProjectRepository(ProjectRepository):
    def __init__(self):
        pass

    def add(self, project: Project) -> None:
        "Add method to be implemented."

    def get(self, uid: str) -> Project:
        "Get method to be implemented."

    def update(self, project: Project) -> None:
        "Update method to be implemented."

    def delete(self, project: Project) -> None:
        "Delete method to be implemented."
