from unittest.mock import Mock, ANY
from click.testing import CliRunner
from taskit.infrastructure.cli.taskit import cli, State


def test_cli_state(state):
    assert isinstance(state, State)


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli, [])
    assert result.exit_code == 0
