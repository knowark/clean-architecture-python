from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli


def test_cli_report_tasks(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['report', 'tasks'], obj=mock_state)
    mock_state.state_reporter.list_tasks.assert_called_with()
    assert result.exit_code == 0
