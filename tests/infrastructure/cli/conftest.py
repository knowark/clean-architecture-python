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
from taskit.application.reporters.state_reporter import (
    StateReporter, MemoryStateReporter)
from taskit.infrastructure.cli.taskit import State


@pytest.fixture
def mock_state() -> Mock:
    mock_state = Mock()
    mock_state.state_reporter.list_tasks.return_value = [{'uid': 'T-1'}]
    mock_state.state_reporter.list_projects.return_value = [{'uid': 'P-1'}]
    return mock_state


@pytest.fixture
def state() -> State:
    project_repository = MemoryProjectRepository()
    task_repository = MemoryTaskRepository()
    agenda_coordinator = AgendaCoordinator(project_repository, task_repository)
    admin_coordinator = AgendaCoordinator(project_repository, task_repository)
    state_reporter = MemoryStateReporter()
    state = State(admin_coordinator, agenda_coordinator, state_reporter)
    return state
