from pytest import fixture
from taskit.application.models.task import Task
from taskit.application.repositories.task_repository import (
    TaskRepository,
    MemoryTaskRepository)


def test_task_repository_methods() -> None:
    abstract_methods = TaskRepository.__abstractmethods__
    assert 'add' in abstract_methods
    assert 'get' in abstract_methods


def test_task_repository_memory_implementation() -> None:
    assert issubclass(MemoryTaskRepository, TaskRepository)


def test_memory_task_repository_load() -> None:
    memory_task_repository = MemoryTaskRepository()
    tasks_dict = {
        'T-1': Task("Buy the milk")
    }
    memory_task_repository.load(tasks_dict)
    assert memory_task_repository.tasks == tasks_dict
