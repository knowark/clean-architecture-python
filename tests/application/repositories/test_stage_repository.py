from pytest import fixture, raises
from taskit.application.models.stage import Stage
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.stage_repository import (
    StageRepository,
    MemoryStageRepository
)


def test_stage_repository_methods() -> None:
    abstract_methods = StageRepository.__abstractmethods__
    assert 'add' in abstract_methods
    assert 'get' in abstract_methods
    assert 'update' in abstract_methods
    assert 'delete' in abstract_methods


def test_stage_repository_memory_implementation() -> None:
    assert issubclass(MemoryStageRepository, StageRepository)


def test_memory_stage_repository_load() -> None:
    memory_stage_repository = MemoryStageRepository()
    stages_dict = {
        'S-1': Stage("New")
    }
    memory_stage_repository.load(stages_dict)
    assert memory_stage_repository.stages == stages_dict


@fixture
def memory_stage_repository() -> MemoryStageRepository:
    memory_stage_repository = MemoryStageRepository()
    stages_dict = {
        'S-1': Stage("New"),
        'S-2': Stage("Progress"),
        'S-3': Stage("Done")
    }
    memory_stage_repository.sequence = 4
    memory_stage_repository.load(stages_dict)
    return memory_stage_repository


def test_memory_stage_repository_get(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = memory_stage_repository.get('S-3')
    assert stage.name == "Done"


def test_memory_stage_repository_get_not_found(
        memory_stage_repository: MemoryStageRepository) -> None:
    with raises(EntityNotFoundError):
        stage = memory_stage_repository.get('MISSING')


def test_memory_stage_repository_add(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = Stage("Analysis")
    memory_stage_repository.add(stage)
    assert len(memory_stage_repository.stages) == 4
    assert memory_stage_repository.stages['S-4'] == stage
    assert memory_stage_repository.sequence == 5


def test_memory_stage_repository_add_with_uid(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = Stage("Development")
    stage.uid = "ABC123"
    memory_stage_repository.add(stage)
    assert len(memory_stage_repository.stages) == 4
    assert memory_stage_repository.stages['ABC123'] == stage
    assert memory_stage_repository.sequence == 5


def test_memory_stage_repository_update(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = Stage("Draft")
    stage.uid = 'S-1'
    assert memory_stage_repository.stages['S-1'].name == "New"
    memory_stage_repository.update(stage)
    assert len(memory_stage_repository.stages) == 3
    assert memory_stage_repository.stages['S-1'].name == "Draft"


def test_memory_stage_repository_update_not_found(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = Stage("Closed")
    stage.uid = 'S-MISSING'
    with raises(EntityNotFoundError):
        memory_stage_repository.update(stage)
    assert len(memory_stage_repository.stages) == 3


def test_memory_stage_repository_delete(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = memory_stage_repository.stages['S-1']
    stage.uid = 'S-1'
    memory_stage_repository.delete(stage)
    assert len(memory_stage_repository.stages) == 2
    assert memory_stage_repository.stages.get('S-1') is None


def test_memory_stage_repository_delete_not_found(
        memory_stage_repository: MemoryStageRepository) -> None:
    stage = Stage("Closed")
    stage.uid = 'S-MISSING'
    with raises(EntityNotFoundError):
        memory_stage_repository.delete(stage)
    assert len(memory_stage_repository.stages) == 3
