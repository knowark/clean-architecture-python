
from datetime import datetime
from pytest import fixture, raises
from taskit.application.models.project import Project
from taskit.application.models.task import Task
from taskit.application.repositories.project_repository import (
    ProjectRepository)
from taskit.application.repositories.task_repository import (
    TaskRepository)
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.coordinators.admin_coordinator import (
    AdminCoordinator)


@fixture
def admin_coordinator(
        project_repository: ProjectRepository,
        task_repository: TaskRepository) -> AdminCoordinator:
    return AdminCoordinator(project_repository, task_repository)


def test_admin_coordinator_creation(
        admin_coordinator: AdminCoordinator) -> None:
    assert hasattr(admin_coordinator, 'create_project')
    assert hasattr(admin_coordinator, 'update_project')


def test_admin_coordinator_create_project(
        admin_coordinator: AdminCoordinator) -> None:
    project_dict = {
        'name': "Workout",
        'comments': "Gym related activities."
    }

    admin_coordinator.create_project(project_dict)

    project_repository = admin_coordinator.project_repository
    project = project_repository.get('P-4')
    assert project.name == project_dict['name']
    assert project.comments == project_dict['comments']


def test_admin_coordinator_update_project(
        admin_coordinator: AdminCoordinator) -> None:
    project_dict = {
        'name': "Academy",
        'uid': 'P-1',
        'comments': "Academy related activities."
    }
    # project_id = project_dict['uid']

    project = admin_coordinator.project_repository.get('P-1')
    assert project.name == "Personal"
    assert project.comments == ""

    admin_coordinator.update_project(project_dict)
    project = admin_coordinator.project_repository.get('P-1')

    assert project.name == "Academy"
    assert project.comments == "Academy related activities."
