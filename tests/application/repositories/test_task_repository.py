from pytest import fixture, raises
from taskit.application.models.task import Task
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.task_repository import (
    TaskRepository,
    MemoryTaskRepository)


def test_task_repository_methods() -> None:
    abstract_methods = TaskRepository.__abstractmethods__  # type: ignore
    assert 'add' in abstract_methods
    assert 'get' in abstract_methods
    assert 'update' in abstract_methods
    assert 'delete' in abstract_methods


def test_task_repository_memory_implementation() -> None:
    assert issubclass(MemoryTaskRepository, TaskRepository)


def test_memory_task_repository_load() -> None:
    memory_task_repository = MemoryTaskRepository()
    tasks_dict = {
        'T-1': Task("Buy the milk")
    }
    memory_task_repository.load(tasks_dict)
    assert memory_task_repository.tasks == tasks_dict


@fixture
def memory_task_repository() -> MemoryTaskRepository:
    memory_task_repository = MemoryTaskRepository()
    tasks_dict = {
        'T-1': Task("Buy the milk"),
        'T-2': Task("Make conference presentation"),
        'T-3': Task("Clean the kitchen")
    }
    memory_task_repository.sequence = 4
    memory_task_repository.load(tasks_dict)
    return memory_task_repository


def test_memory_task_repository_get(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = memory_task_repository.get('T-3')
    assert task.name == "Clean the kitchen"


def test_memory_task_repository_get_not_found(
        memory_task_repository: MemoryTaskRepository) -> None:
    with raises(EntityNotFoundError):
        memory_task_repository.get('MISSING')


def test_memory_task_repository_add(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = Task("Improve the repository")
    memory_task_repository.add(task)
    assert len(memory_task_repository.tasks) == 4
    assert memory_task_repository.tasks['T-4'] == task
    assert memory_task_repository.sequence == 5


def test_memory_task_repository_add_with_uid(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = Task("Improve the repository")
    task.uid = "ABC123"
    memory_task_repository.add(task)
    assert len(memory_task_repository.tasks) == 4
    assert memory_task_repository.tasks['ABC123'] == task
    assert memory_task_repository.sequence == 5


def test_memory_task_repository_update(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = Task("Buy the milk and the eggs")
    task.uid = 'T-1'
    assert memory_task_repository.tasks['T-1'].name == "Buy the milk"
    memory_task_repository.update(task)
    assert len(memory_task_repository.tasks) == 3
    assert memory_task_repository.tasks['T-1'].name == (
        "Buy the milk and the eggs")


def test_memory_task_repository_update_not_found(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = Task("Fix my bike")
    task.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        memory_task_repository.update(task)
    assert len(memory_task_repository.tasks) == 3


def test_memory_task_repository_delete(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = memory_task_repository.tasks['T-1']
    task.uid = 'T-1'
    memory_task_repository.delete(task)
    assert len(memory_task_repository.tasks) == 2
    assert memory_task_repository.tasks.get('T-1') is None


def test_memory_task_repository_delete_not_found(
        memory_task_repository: MemoryTaskRepository) -> None:
    task = Task("Fix my bike")
    task.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        memory_task_repository.delete(task)
    assert len(memory_task_repository.tasks) == 3
