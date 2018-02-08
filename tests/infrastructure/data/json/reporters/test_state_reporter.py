from pytest import fixture
from taskit.application.reporters.state_reporter import StateReporter
from taskit.infrastructure.data.json.reporters.state_reporter import (
    JsonStateReporter
)


@fixture
def json_state_reporter(json_file) -> JsonStateReporter:
    json_state_reporter = JsonStateReporter(json_file)
    return json_state_reporter


def test_json_state_reporter_creation(json_state_reporter):
    assert isinstance(json_state_reporter, StateReporter)


def test_json_state_reporter_list_tasks(json_state_reporter):
    result = json_state_reporter.list_tasks()
    assert len(result) == 3
    for task_dict in result:
        assert task_dict.get('uid')
        assert task_dict.get('name')

def test_json_state_reporter_list_tasks_in_project(json_state_reporter):
    result = json_state_reporter.list_tasks_in_project('P-1')
    assert len(result) == 2
    uid_list = [task_dict['uid'] for task_dict in result]
    assert 'T-1' in uid_list
    assert 'T-3' in uid_list

def test_json_state_reporter_list_tasks_in_stage(json_state_reporter):
    result = json_state_reporter.list_tasks_in_stage('Done')
    assert len(result) == 1
    uid_list = [task_dict['uid'] for task_dict in result]
    assert 'T-3' in uid_list

def test_json_state_reporter_list_projects(json_state_reporter):
    result = json_state_reporter.list_projects()
    assert len(result) == 3
    for task_dict in result:
        assert task_dict.get('uid')
        assert task_dict.get('name')