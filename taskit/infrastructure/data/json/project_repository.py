import json
from taskit.application.models.project import Project
from taskit.application.repositories.project_repository import ProjectRepository


class JsonProjectRepository(ProjectRepository):
    def __init__(self, filename):
        self.filename = filename

    def add(self, project: Project) -> None:
        "Add method to be implemented."

    def get(self, uid: str) -> Project:
        with open(self.filename) as f:
            data = json.load(f)
            projects = data.get('projects', {})
        project_dict = projects.get(uid)
        return Project(**project_dict)

    def update(self, project: Project) -> None:
        "Update method to be implemented."

    def delete(self, project: Project) -> None:
        "Delete method to be implemented."
