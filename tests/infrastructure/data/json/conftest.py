import json
from datetime import date, datetime
from pytest import fixture
from taskit.application.models.project import Project
from taskit.application.models.task import Task
from taskit.infrastructure.data.json import json_serialize


@fixture
def json_file(tmpdir_factory):
    file_name = tmpdir_factory.mktemp('data').join('taskit.json')
    test_dictionary = {
        "projects": {
            'P-1': vars(Project("Personal", uid="P-1")),
            'P-2': vars(Project("Work", uid="P-2")),
            'P-3': vars(Project("Errands", uid="P-3"))
        },
        "tasks": {
            'T-1': vars(Task("Buy the milk",
                             uid="T-1", project_id="P-1", stage="New")),
            'T-2': vars(Task("Make conference presentation",
                             uid="T-2", project_id="P-2", stage="Progress")),
            'T-3': vars(Task("Clean the kitchen",
                             uid="T-3", project_id="P-1", stage="Done"))
        },
        "_sequences": {
            "projects": 4,
            "tasks": 4
        }
    }
    with open(str(file_name), 'w+') as f:
        json.dump(test_dictionary, f, default=json_serialize)
    return str(file_name)
