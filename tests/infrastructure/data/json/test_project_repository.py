from taskit.application.repositories.project_repository import ProjectRepository
from taskit.infrastructure.data.json.project_repository import (
    JsonProjectRepository)


def test_json_repository_creation():
    project_repository = JsonProjectRepository()
    assert isinstance(project_repository, ProjectRepository)
