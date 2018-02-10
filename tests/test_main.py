import os
import sys
import taskit.__main__
from subprocess import run
from pytest import fixture
from unittest.mock import Mock, patch
from taskit.__main__ import main, build_state


@fixture(scope='module')
def taskit_dir(tmpdir_factory: fixture) -> str:
    taskit_dir = tmpdir_factory.mktemp('taskitdir')
    return str(taskit_dir)


def test_main(taskit_dir) -> None:
    sandbox = patch.dict(os.environ, {'TASKIT_DIR': taskit_dir})
    sandbox.start()
    python_bin = sys.executable
    result = run([python_bin, '-m', 'taskit'])
    sandbox.stop()
    assert result.returncode == 0


def test_main_db_file_not_empty(taskit_dir) -> None:
    sandbox = patch.dict(os.environ, {'TASKIT_DIR': taskit_dir})
    sandbox.start()
    db_path = os.sep.join([taskit_dir, 'db.json'])
    with open(db_path, 'w+') as f:
        f.write('{"projects": {}}')
    python_bin = sys.executable
    result = run([python_bin, '-m', 'taskit'])
    sandbox.stop()
    assert result.returncode == 0


def test_main_exception_handling(taskit_dir, monkeypatch) -> None:
    sandbox = patch.dict(os.environ, {'TASKIT_DIR': taskit_dir})
    sandbox.start()
    monkeypatch.setattr("taskit.__main__.build_state", lambda x: "NOTHING")
    python_bin = sys.executable
    result = run([python_bin, '-m', 'taskit', 'report', 'tasks'])
    sandbox.stop()
    assert result.returncode != 0
