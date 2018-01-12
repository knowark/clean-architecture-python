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
