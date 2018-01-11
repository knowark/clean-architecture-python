import datetime
import pytest
from taskit.application.models.task import Task


@pytest.fixture
def task() -> pytest.fixture:
    name = "Buy the milk"
    return Task(name=name)


def test_task_creation(task: pytest.fixture) -> None:
    assert task.name == "Buy the milk"


def test_task_default_attributes(task: pytest.fixture) -> None:
    assert task.uid == ""
    assert isinstance(task.due_date, datetime.datetime)
    assert task.priority == 1
    assert task.project_id == ""
    assert task.stage_id == ""
    assert task.comments == ""
