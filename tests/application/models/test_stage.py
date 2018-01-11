import datetime
import pytest
from taskit.application.models.stage import Stage


@pytest.fixture
def stage() -> pytest.fixture:
    name = "backlog"
    return Stage(name=name)


def test_stage_creation(stage: pytest.fixture) -> None:
    assert stage.name == "backlog"


def test_stage_default_attributes(stage: pytest.fixture) -> None:
    assert stage.uid == ""
    assert stage.closure is False
