import json
from taskit.application.models.project import Project
from taskit.application.repositories.errors import EntityNotFoundError
from taskit.application.repositories.project_repository import ProjectRepository
from taskit.infrastructure.data.json import json_serialize


class JsonProjectRepository(ProjectRepository):
    def __init__(self, filename):
        self.filename = filename

    def add(self, project: Project) -> None:
        with open(self.filename, 'r') as f:
            data = json.load(f)
        sequence = data.get('_sequences', {}).get('projects', 1)
        project.uid = project.uid or ("P-" + str(sequence))
        data['projects'][project.uid] = vars(project)
        data['_sequences']['projects'] = sequence + 1
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=json_serialize)

    def get(self, uid: str) -> Project:
        with open(self.filename) as f:
            data = json.load(f)
            projects = data.get('projects', {})
        project_dict = projects.get(uid)
        if not project_dict:
            raise EntityNotFoundError(
                "The project was not found in file.")
        return Project(**project_dict)

    def update(self, project: Project) -> None:
        uid = project.uid
        with open(self.filename) as f:
            data = json.load(f)
            projects = data.get('projects', {})
        old_project = projects.get(uid)
        if not old_project:
            raise EntityNotFoundError("Project not found.")
        data['projects'][project.uid] = vars(project)
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=json_serialize)

    def delete(self, project: Project) -> None:
        uid = project.uid
        with open(self.filename) as f:
            data = json.load(f)
            projects = data.get('projects', {})
        old_project = projects.get(uid)
        if not old_project:
            raise EntityNotFoundError("Project not found.")
        del data['projects'][project.uid]
        with open(self.filename, 'w') as f:
            json.dump(data, f, default=json_serialize)
