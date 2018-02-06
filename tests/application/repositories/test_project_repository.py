from pytest import fixture, raises
from taskit.application.models.project import Project
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.project_repository import (
    ProjectRepository,
    MemoryProjectRepository)


def test_project_repository_methods() -> None:
    abstract_methods = ProjectRepository.__abstractmethods__  # type: ignore
    assert 'add' in abstract_methods
    assert 'get' in abstract_methods
    assert 'update' in abstract_methods
    assert 'delete' in abstract_methods


def test_project_repository_memory_implementation() -> None:
    assert issubclass(MemoryProjectRepository, ProjectRepository)


def test_memory_project_repository_load() -> None:
    memory_project_repository = MemoryProjectRepository()
    projects_dict = {
        'P-1': Project("Personal")
    }
    memory_project_repository.load(projects_dict)
    assert memory_project_repository.projects == projects_dict


@fixture
def memory_project_repository() -> MemoryProjectRepository:
    memory_project_repository = MemoryProjectRepository()
    projects_dict = {
        'P-1': Project("Personal"),
        'P-2': Project("Work"),
        'P-3': Project("Errands")
    }
    memory_project_repository.sequence = 4
    memory_project_repository.load(projects_dict)
    return memory_project_repository


def test_memory_project_repository_get(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = memory_project_repository.get('P-3')
    assert project.name == "Errands"


def test_memory_project_repository_get_not_found(
        memory_project_repository: MemoryProjectRepository) -> None:
    with raises(EntityNotFoundError):
        memory_project_repository.get('MISSING')


def test_memory_project_repository_add(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = Project("Shopping")
    memory_project_repository.add(project)
    assert len(memory_project_repository.projects) == 4
    assert memory_project_repository.projects['P-4'] == project
    assert memory_project_repository.sequence == 5


def test_memory_project_repository_add_with_uid(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = Project("General")
    project.uid = "ABC123"
    memory_project_repository.add(project)
    assert len(memory_project_repository.projects) == 4
    assert memory_project_repository.projects['ABC123'] == project
    assert memory_project_repository.sequence == 5


def test_memory_project_repository_update(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = Project("Personal & Family")
    project.uid = 'P-1'
    assert memory_project_repository.projects['P-1'].name == "Personal"
    memory_project_repository.update(project)
    assert len(memory_project_repository.projects) == 3
    assert memory_project_repository.projects['P-1'].name == (
        "Personal & Family")


def test_memory_project_repository_update_not_found(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = Project("Fix my bike")
    project.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        memory_project_repository.update(project)
    assert len(memory_project_repository.projects) == 3


def test_memory_project_repository_delete(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = memory_project_repository.projects['P-1']
    project.uid = 'P-1'
    memory_project_repository.delete(project)
    assert len(memory_project_repository.projects) == 2
    assert memory_project_repository.projects.get('P-1') is None


def test_memory_project_repository_delete_not_found(
        memory_project_repository: MemoryProjectRepository) -> None:
    project = Project("Fix my bike")
    project.uid = 'T-MISSING'
    with raises(EntityNotFoundError):
        memory_project_repository.delete(project)
    assert len(memory_project_repository.projects) == 3
