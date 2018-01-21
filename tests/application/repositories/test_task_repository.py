from taskit.application.repositories.task_repository import TaskRepository


def test_task_repository_methods() -> None:
    abstract_methods = TaskRepository.__abstractmethods__
    assert 'add' in abstract_methods
    assert 'get' in abstract_methods
