from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli


def test_cli_admin_new_project(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['admin', 'new', 'project'], obj=mock_state, input="Academic\n")
    project_dict = {
        'name': "Academic"
    }
    mock_state.admin_coordinator.create_project.assert_called_with(
        project_dict)
    assert result.exit_code == 0


def test_cli_admin_update_project(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['admin', 'update', 'project'],
        obj=mock_state, input="P-1\nAcademic\n")
    project_dict = {
        'uid': "P-1",
        'name': "Academic"
    }
    mock_state.admin_coordinator.update_project.assert_called_with(
        project_dict)
    assert result.exit_code == 0


def test_cli_admin_update_task(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['admin', 'update', 'task'],
        obj=mock_state, input="T-1\nBuy chocolates\n")
    project_dict = {
        'uid': "T-1",
        'name': "Buy chocolates"
    }
    mock_state.admin_coordinator.update_task.assert_called_with(
        project_dict)
    assert result.exit_code == 0


def test_cli_admin_delete_project(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['admin', 'delete', 'project'],
        obj=mock_state, input="P-1\n")
    mock_state.admin_coordinator.delete_project.assert_called_with(
        "P-1")
    assert result.exit_code == 0


def test_cli_admin_delete_task(mock_state: Mock):
    runner = CliRunner()
    result = runner.invoke(
        cli, ['admin', 'delete', 'task'],
        obj=mock_state, input="T-1\n")
    mock_state.admin_coordinator.delete_task.assert_called_with(
        "T-1")
    assert result.exit_code == 0
