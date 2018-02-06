import pytest
from unittest.mock import Mock


@pytest.fixture
def state() -> Mock:
    state = Mock()
    return state
