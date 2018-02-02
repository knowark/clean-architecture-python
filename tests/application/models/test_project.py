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


def test_project_initilization_from_dict():
    project_dict = {
        'name': "Done",
        'uid': "S-001",
        'stage_ids': ['Draft', 'Progress', 'Done'],
        'comments': "This is the final stage."
    }

    project = Project(**project_dict)
    assert project.name == "Done"
    assert project.uid == "S-001"
    assert project.stage_ids == ['Draft', 'Progress', 'Done']
    assert project.comments == "This is the final stage."
