import os
import sys
from pathlib import Path
from taskit.application.coordinators.admin_coordinator import (
    AdminCoordinator)
from taskit.application.coordinators.agenda_coordinator import (
    AgendaCoordinator)
from taskit.infrastructure.data.json.repositories.project_repository import (
    JsonProjectRepository)
from taskit.infrastructure.data.json.repositories.task_repository import (
    JsonTaskRepository)
from taskit.infrastructure.data.json.reporters.state_reporter import (
    JsonStateReporter)
from taskit.infrastructure.cli.taskit import cli, State


def prepare_json_database(taskit_dir: str) -> str:
    os.makedirs(taskit_dir, exist_ok=True)
    db_path = os.sep.join([taskit_dir, 'db.json'])
    with open(db_path, 'a+') as f:
        f.seek(0)
        contents = f.read()
        if not contents:
            f.write(""" 
            {
                "projects": {},
                "tasks": {},
                "_sequences": {}
            }
            """)
    return db_path


def build_state(json_file: str) -> State:
    project_repository = JsonProjectRepository(json_file)
    task_repository = JsonTaskRepository(json_file)
    agenda_coordinator = AgendaCoordinator(project_repository, task_repository)
    admin_coordinator = AdminCoordinator(project_repository, task_repository)
    state_reporter = JsonStateReporter(json_file)
    state = State(admin_coordinator, agenda_coordinator, state_reporter)
    return state


def main():
    taskit_dir = (
        os.environ.get('TASKIT_DIR') or str(Path.home().joinpath('.taskit'))
    )
    db_file = prepare_json_database(taskit_dir)
    state = build_state(db_file)

    try:
        cli(obj=state)
    except Exception as e:
        print("\nEXECUTION ERROR:", e)
        sys.exit(-1)


if __name__ == '__main__':
    main()
