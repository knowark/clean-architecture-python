from taskit.application.coordinators.agenda_coordinator import (
    AgendaCoordinator)


def test_agenda_coordinator_creation():
    agenda_coordinator = AgendaCoordinator()
    assert hasattr(agenda_coordinator, 'create_new_task')
