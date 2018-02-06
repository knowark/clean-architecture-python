from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli, State


def test_cli_agenda_new(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['agenda', 'new'], obj=mock_state, input="Pay the bills\n")
    task_dict = {
        'name': "Pay the bills"
    }
    mock_state.agenda_coordinator.create_task.assert_called_with(task_dict)
    assert result.exit_code == 0
