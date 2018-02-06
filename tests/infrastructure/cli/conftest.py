import pytest
from unittest.mock import Mock
from taskit.application.repositories.project_repository import (
    MemoryProjectRepository)
from taskit.application.repositories.task_repository import (
    MemoryTaskRepository)
from taskit.application.coordinators.admin_coordinator import (
    AdminCoordinator)
from taskit.application.coordinators.agenda_coordinator import (
    AgendaCoordinator)
from taskit.infrastructure.cli.taskit import State


@pytest.fixture
def mock_state() -> Mock:
    mock_state = Mock()
    return mock_state


@pytest.fixture
def state() -> State:
    project_repository = MemoryProjectRepository()
    task_repository = MemoryTaskRepository()
    agenda_coordinator = AgendaCoordinator(project_repository, task_repository)
    admin_coordinator = AgendaCoordinator(project_repository, task_repository)
    state = State(admin_coordinator, agenda_coordinator)
    return state
