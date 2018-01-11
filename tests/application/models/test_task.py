import taskit
from taskit.application.models.task import Task


def test_task_creation() -> None:
    name = "Buy the milk"

    task = Task(name=name)

    assert task.name == name
