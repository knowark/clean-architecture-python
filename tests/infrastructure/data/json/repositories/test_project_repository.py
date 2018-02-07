import json
from pytest import fixture, raises
from taskit.application.models.project import Project
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.project_repository import ProjectRepository
from taskit.infrastructure.data.json.repositories.project_repository import (
    JsonProjectRepository)


@fixture
def json_project_repository(json_file: str) -> JsonProjectRepository:
    json_project_repository = JsonProjectRepository(json_file)
    json_project_repository.sequence = 4
    return json_project_repository


def test_json_project_repository_creation(
        json_project_repository: JsonProjectRepository):
    assert isinstance(json_project_repository, ProjectRepository)


def test_json_project_repository_get(
        json_project_repository: JsonProjectRepository) -> None:
    project = json_project_repository.get('P-3')
    assert project.name == "Errands"


def test_json_project_repository_get_not_found(
        json_project_repository: JsonProjectRepository) -> None:
    with raises(EntityNotFoundError):
        json_project_repository.get('MISSING')


def test_json_project_repository_add(
        json_project_repository: JsonProjectRepository) -> None:
    project = Project("Shopping")
    json_project_repository.add(project)
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['projects']) == 4
    assert data['projects']['P-4']['uid'] == project.uid
    assert data['projects']['P-4']['name'] == project.name
    assert data['_sequences']['projects'] == 5


def test_json_project_repository_add_with_uid(
        json_project_repository: JsonProjectRepository) -> None:
    project = Project("General")
    project.uid = "ABC123"
    json_project_repository.add(project)
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['projects']) == 4
    assert data['projects']['ABC123']['uid'] == project.uid
    assert data['projects']['ABC123']['name'] == project.name
    assert data['_sequences']['projects'] == 5


def test_json_project_repository_update(
        json_project_repository: JsonProjectRepository) -> None:
    project = Project("Personal & Family")
    project.uid = 'P-1'
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert data['projects']['P-1']['name'] == "Personal"
    json_project_repository.update(project)
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['projects']) == 3
    assert data['projects']['P-1']['name'] == "Personal & Family"


def test_json_project_repository_update_not_found(
        json_project_repository: JsonProjectRepository) -> None:
    project = Project("Hobbies")
    project.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        json_project_repository.update(project)
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['projects']) == 3


def test_json_project_repository_delete(
        json_project_repository: JsonProjectRepository) -> None:
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    project_dict = data['projects']['P-1']
    project = Project(**project_dict)
    json_project_repository.delete(project)
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['projects']) == 2
    assert 'P-1' not in data['projects']


def test_json_project_repository_delete_not_found(
        json_project_repository: JsonProjectRepository) -> None:
    project = Project("Hobbies")
    project.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        json_project_repository.delete(project)
    with open(json_project_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['projects']) == 3
