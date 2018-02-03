from typing import Dict
from taskit.application.models.task import Task
from taskit.application.repositories.project_repository import ProjectRepository
from taskit.application.repositories.task_repository import TaskRepository


class AgendaCoordinator:
    def __init__(self, project_repository: ProjectRepository,
                 task_repository: TaskRepository) -> None:
        self.task_repository = task_repository
        self.project_repository = project_repository

    def create_task(self, task_dict: Dict[str, any]):
        project_id = task_dict.get('project_id')
        # Validate that the project exists
        self.project_repository.get(project_id)

        # Intantiate a Task object
        task = Task(**task_dict)

        # Set the task stage to 'new'
        task.stage = 'new' 

        # Add the new task to the task repository
        self.task_repository.add(task)



        
