from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli, State
from taskit.application.repositories.project_repository import (
    MemoryProjectRepository)


def test_cli_agenda_new(state: Mock):
    runner = CliRunner()
    runner.invoke(cli, ['agenda', 'new'], obj=state)
    state.agenda_coordinator.create_task.assert_called_with(ANY)
