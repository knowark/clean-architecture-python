from abc import ABC, abstractmethod
from typing import List, Dict


class StateReporter(ABC):

    @abstractmethod
    def list_tasks(self, offset=0, limit=10) -> List[Dict[str, str]]:
        """List all the persisted tasks"""

    @abstractmethod
    def list_tasks_in_project(self, project_id: str) -> List[Dict[str, str]]:
        """List the tasks belonging the same project."""

    @abstractmethod
    def list_tasks_in_stage(self, stage: str) -> List[Dict[str, str]]:
        """List the tasks belonging the same stage."""

    @abstractmethod
    def list_projects(self, offset=0, limit=10) -> List[Dict[str, str]]:
        """List all the persisted projects"""


class MemoryStateReporter(StateReporter):

    def list_tasks(self, offset=0, limit=10) -> List[Dict[str, str]]:
        """List all the persisted tasks"""

    def list_tasks_in_project(self, project_id: str) -> List[Dict[str, str]]:
        """List the tasks belonging the same project."""

    def list_tasks_in_stage(self, stage: str) -> List[Dict[str, str]]:
        """List the tasks belonging the same stage."""

    def list_projects(self, offset=0, limit=10) -> List[Dict[str, str]]:
        """List all the persisted projects"""
