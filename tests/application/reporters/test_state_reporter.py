from taskit.application.reporters.state_reporter import StateReporter


def test_state_reporter_methods() -> None:
    abstract_methods = StateReporter.__abstractmethods__  # type: ignore
    assert 'list_tasks' in abstract_methods
    assert 'list_tasks_in_project' in abstract_methods
    assert 'list_tasks_in_stage' in abstract_methods
    assert 'list_projects' in abstract_methods
