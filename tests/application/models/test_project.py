from pytest import fixture
from taskit.application.models.project import Project


@fixture
def project() -> Project:
    name = "Personal"
    return Project(name=name)


def test_project_creation(project: Project) -> None:
    assert project.name == "Personal"


def test_project_default_attributes(project: Project) -> None:
    assert project.uid == ""
    assert project.stage_ids == []
    assert project.comments == ""
