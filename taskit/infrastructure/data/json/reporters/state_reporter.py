import json
from typing import List, Dict
from taskit.application.reporters.state_reporter import StateReporter


class JsonStateReporter(StateReporter):
    def __init__(self, filename):
        self.filename = filename

    def list_tasks(self, offset=0, limit=10) -> List[Dict[str, str]]:
        with open(self.filename) as f:
            data = json.load(f)
        tasks = data['tasks']
        result = sorted(list(tasks.values()), key=lambda x: x['uid'])
        return result[offset:limit]

    def list_tasks_in_project(self, project_id: str) -> List[Dict[str, str]]:
        with open(self.filename) as f:
            data = json.load(f)
        tasks = data['tasks']
        result = [
            task for task in tasks.values() if task['project_id'] == project_id]
        return result

    def list_tasks_in_stage(self, stage: str) -> List[Dict[str, str]]:
        with open(self.filename) as f:
            data = json.load(f)
        tasks = data['tasks']
        result = [
            task for task in tasks.values() if task['stage'] == stage]
        return result

    def list_projects(self, offset=0, limit=10) -> List[Dict[str, str]]:
        with open(self.filename) as f:
            data = json.load(f)
        projects = data['projects']
        result = sorted(list(projects.values()), key=lambda x: x['uid'])
        return result[offset:limit]

