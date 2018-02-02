
from datetime import datetime
from pytest import fixture
from taskit.application.coordinators.agenda_coordinator import (
    AgendaCoordinator)


@fixture
def agenda_coordinator() -> AgendaCoordinator:
    return AgendaCoordinator()


def test_agenda_coordinator_creation(
        agenda_coordinator: AgendaCoordinator) -> None:
    assert hasattr(agenda_coordinator, 'create_new_task')


# def test_aqenda_coordinator_create_new_task(
#         self, agenda_coordinator: AgendaCoordinator) -> None:
#     task_dict = {
#         'name': "Buy bread and eggs",
#         'due_date':  datetime.strptime("2018-02-15", '%Y-%m-%d'),
#         'priority': 3,
#         'project_id': "P-1",
#         'stage_id': "S-1",
#         'comments': "The supermarket closes at 8 pm."
#     }

#     agenda_coordinator.create_new_task(task_dict)
    
