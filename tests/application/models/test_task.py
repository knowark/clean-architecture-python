from datetime import datetime
from pytest import fixture
from taskit.application.models.task import Task


@fixture
def task() -> Task:
    name = "Buy the milk"
    return Task(name=name)


def test_task_creation(task: Task) -> None:
    assert task.name == "Buy the milk"


def test_task_default_attributes(task: Task) -> None:
    assert task.uid == ""
    assert isinstance(task.due_date, datetime)
    assert task.priority == 1
    assert task.project_id == ""
    assert task.stage == ""
    assert task.comments == ""
