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
    assert project.comments == ""


def test_project_initilization_from_dict():
    project_dict = {
        'name': "Business",
        'uid': "P-001",
        'comments': "Management of business oportunities."
    }

    project = Project(**project_dict)
    assert project.name == "Business"
    assert project.uid == "P-001"
    assert project.comments == "Management of business oportunities."
