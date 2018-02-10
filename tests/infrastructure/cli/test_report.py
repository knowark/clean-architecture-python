from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli


def test_cli_report_tasks(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['report', 'tasks'], obj=mock_state)
    mock_state.state_reporter.list_tasks.assert_called_with()
    assert result.exit_code == 0


def test_cli_report_tasks_in_project(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['report', 'tasks', '--project_id=P-1'], obj=mock_state)
    mock_state.state_reporter.list_tasks_in_project.assert_called_with(ANY)
    assert result.exit_code != 0


def test_cli_report_tasks_in_stage(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['report', 'tasks', '--stage=New'], obj=mock_state)
    mock_state.state_reporter.list_tasks_in_stage.assert_called_with(ANY)
    assert result.exit_code != 0


def test_cli_report_projects(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['report', 'projects'], obj=mock_state)
    mock_state.state_reporter.list_projects.assert_called_with()
    assert result.exit_code == 0
