import pytest
from taskit.application.models.project import Project


@pytest.fixture
def project() -> pytest.fixture:
    name = "Personal"
    return Project(name=name)


def test_project_creation(project: pytest.fixture) -> None:
    assert project.name == "Personal"


def test_project_default_attributes(project: pytest.fixture) -> None:
    assert project.uid == ""
    assert project.stage_ids == []
    assert project.comments == ""
