import json
from pytest import fixture, raises
from taskit.application.models.task import Task
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.task_repository import TaskRepository
from taskit.infrastructure.data.json.repositories.task_repository import (
    JsonTaskRepository)


@fixture
def json_task_repository(json_file: str) -> JsonTaskRepository:
    json_task_repository = JsonTaskRepository(json_file)
    json_task_repository.sequence = 4
    return json_task_repository


def test_json_task_repository_creation(
        json_task_repository: JsonTaskRepository):
    assert isinstance(json_task_repository, TaskRepository)


def test_json_task_repository_get(
        json_task_repository: JsonTaskRepository) -> None:
    task = json_task_repository.get('T-3')
    assert task.name == "Clean the kitchen"


def test_json_task_repository_get_not_found(
        json_task_repository: JsonTaskRepository) -> None:
    with raises(EntityNotFoundError):
        json_task_repository.get('MISSING')


def test_json_task_repository_add(
        json_task_repository: JsonTaskRepository) -> None:
    task = Task("Organize my documents")
    json_task_repository.add(task)
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['tasks']) == 4
    assert data['tasks']['T-4']['uid'] == task.uid
    assert data['tasks']['T-4']['name'] == task.name
    assert data['_sequences']['tasks'] == 5


def test_json_task_repository_add_with_uid(
        json_task_repository: JsonTaskRepository) -> None:
    task = Task("General")
    task.uid = "ABC123"
    json_task_repository.add(task)
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['tasks']) == 4
    assert data['tasks']['ABC123']['uid'] == task.uid
    assert data['tasks']['ABC123']['name'] == task.name
    assert data['_sequences']['tasks'] == 5


def test_json_task_repository_update(
        json_task_repository: JsonTaskRepository) -> None:
    task = Task("Buy the milk and eggs")
    task.uid = 'T-1'
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert data['tasks']['T-1']['name'] == "Buy the milk"
    json_task_repository.update(task)
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['tasks']) == 3
    assert data['tasks']['T-1']['name'] == "Buy the milk and eggs"


def test_json_task_repository_update_not_found(
        json_task_repository: JsonTaskRepository) -> None:
    task = Task("Fix my bike")
    task.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        json_task_repository.update(task)
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['tasks']) == 3


def test_json_task_repository_delete(
        json_task_repository: JsonTaskRepository) -> None:
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    task_dict = data['tasks']['T-1']
    task = Task(**task_dict)
    json_task_repository.delete(task)
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['tasks']) == 2
    assert 'T-1' not in data['tasks']


def test_json_task_repository_delete_not_found(
        json_task_repository: JsonTaskRepository) -> None:
    task = Task("Fix my bike")
    task.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        json_task_repository.delete(task)
    with open(json_task_repository.filename, 'r') as f:
        data = json.load(f)
    assert len(data['tasks']) == 3
