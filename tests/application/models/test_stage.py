from pytest import fixture
from taskit.application.models.stage import Stage


@fixture
def stage() -> Stage:
    name = "backlog"
    return Stage(name=name)


def test_stage_creation(stage: Stage) -> None:
    assert stage.name == "backlog"


def test_stage_default_attributes(stage: Stage) -> None:
    assert stage.uid == ""
    assert stage.closure is False


def test_stage_initilization_from_dict():
    stage_dict = {
        'name': "Done",
        'uid': "S-001",
        'closure': True
    }
    stage = Stage(**stage_dict)
    assert stage.name == "Done"
    assert stage.uid == "S-001"
    assert stage.closure is True
