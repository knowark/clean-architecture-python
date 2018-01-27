from abc import ABC, abstractmethod
from typing import Dict, Optional
from taskit.application.models.stage import Stage
from taskit.application.repositories.errors import EntityNotFoundError


class StageRepository(ABC):
    @abstractmethod
    def add(self, stage: Stage) -> None:
        "Add method to be implemented."

    @abstractmethod
    def get(self, uid: str) -> Stage:
        "Get method to be implemented."

    @abstractmethod
    def update(self, stage: Stage) -> None:
        "Update method to be implemented."

    @abstractmethod
    def delete(self, stage: Stage) -> None:
        "Delete method to be implemented."


class MemoryStageRepository(StageRepository):
    def __init__(self) -> None:
        self.stages = {}  # type: Dict[str, Stage]
        self.sequence = 1

    def add(self, stage: Stage) -> None:
        stage.uid = stage.uid or ("S-" + str(self.sequence))
        self.stages[stage.uid] = stage
        self.sequence += 1

    def get(self, uid: str) -> Stage:
        stage = self.stages.get(uid)
        if not stage:
            raise EntityNotFoundError("Stage not found.")
        return stage

    def update(self, stage: Stage) -> None:
        uid = stage.uid
        old_stage = self.stages.get(uid)
        if not old_stage:
            raise EntityNotFoundError("Stage not found.")
        self.stages[uid] = stage

    def delete(self, stage: Stage) -> None:
        uid = stage.uid
        old_stage = self.stages.get(uid)
        if not old_stage:
            raise EntityNotFoundError("Stage not found.")
        del self.stages[uid]

    def load(self, stages_dict: Dict[str, Stage]) -> None:
        self.stages = stages_dict
