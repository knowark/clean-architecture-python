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
    assert task.stage_id == ""
    assert task.comments == ""


def test_task_initilization_from_dict():
    now = datetime.now()
    task_dict = {
        'name': "Go to the gym",
        'uid': "T-007",
        'due_date': now,
        'priority': 3,
        'project_id': "P-001",
        'stage_id': "S-003",
        'comments': "Don't hesitate. Do it!"
    }
    task = Task(**task_dict)
    assert task.name == "Go to the gym"
    assert task.uid == "T-007"
    assert task.due_date == now
    assert task.priority == 3
    assert task.project_id == "P-001"
    assert task.stage_id == "S-003"
    assert task.comments == "Don't hesitate. Do it!"
