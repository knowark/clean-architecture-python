from pytest import fixture, raises
from taskit.application.models.project import Project
from taskit.application.models.task import Task
from taskit.application.repositories.project_repository import (
    ProjectRepository, MemoryProjectRepository)
from taskit.application.repositories.task_repository import (
    TaskRepository, MemoryTaskRepository)


@fixture
def project_repository() -> MemoryProjectRepository:
    project_repository = MemoryProjectRepository()
    projects_dict = {
        'P-1': Project("Personal"),
        'P-2': Project("Work"),
        'P-3': Project("Errands")
    }
    project_repository.sequence = 4
    project_repository.load(projects_dict)
    return project_repository


@fixture
def task_repository() -> MemoryTaskRepository:
    task_repository = MemoryTaskRepository()
    tasks_dict = {
        'T-1': Task("Buy the milk"),
        'T-2': Task("Make conference presentation"),
        'T-3': Task("Clean the kitchen")
    }
    task_repository.sequence = 4
    task_repository.load(tasks_dict)
    return task_repository
