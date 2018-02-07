import json
from taskit.application.models.task import Task
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.task_repository import TaskRepository
from taskit.infrastructure.data.json import json_serialize


class JsonTaskRepository(TaskRepository):
    def __init__(self, filename):
        self.filename = filename

    def add(self, task: Task) -> None:
        with open(self.filename, 'r') as f:
            data = json.load(f)
        sequence = data.get('_sequences', {}).get('tasks', 1)
        task.uid = task.uid or ("T-" + str(sequence))
        data['tasks'][task.uid] = vars(task)
        data['_sequences']['tasks'] = sequence + 1
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=json_serialize)

    def get(self, uid: str) -> Task:
        with open(self.filename) as f:
            data = json.load(f)
            tasks = data.get('tasks', {})
        task_dict = tasks.get(uid)
        if not task_dict:
            raise EntityNotFoundError(
                "The task was not found in file.")
        return Task(**task_dict)

    def update(self, task: Task) -> None:
        uid = task.uid
        with open(self.filename) as f:
            data = json.load(f)
            tasks = data.get('tasks', {})
        old_task = tasks.get(uid)
        if not old_task:
            raise EntityNotFoundError("Task not found.")
        data['tasks'][task.uid] = vars(task)
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=json_serialize)

    def delete(self, task: Task) -> None:
        uid = task.uid
        with open(self.filename) as f:
            data = json.load(f)
            tasks = data.get('tasks', {})
        old_task = tasks.get(uid)
        if not old_task:
            raise EntityNotFoundError("Task not found.")
        del data['tasks'][task.uid]
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=json_serialize)
