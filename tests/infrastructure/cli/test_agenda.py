from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli, State


def test_cli_agenda_new(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['agenda', 'new'], obj=mock_state, input="Pay the bills\nP-1\n")
    task_dict = {
        'name': "Pay the bills",
        'project_id': 'P-1'
    }
    mock_state.agenda_coordinator.create_task.assert_called_with(task_dict)
    assert result.exit_code == 0


def test_cli_agenda_start(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['agenda', 'start'], obj=mock_state, input="T-1\n")
    mock_state.agenda_coordinator.start_task.assert_called_with("T-1")
    assert result.exit_code == 0


def test_cli_agenda_complete(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['agenda', 'complete'], obj=mock_state, input="T-1\n")
    mock_state.agenda_coordinator.complete_task.assert_called_with("T-1")
    assert result.exit_code == 0
