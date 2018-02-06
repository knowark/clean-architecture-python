import click
from taskit.application.coordinators.admin_coordinator import AdminCoordinator
from taskit.application.coordinators.agenda_coordinator import AgendaCoordinator
from taskit.infrastructure.cli.admin import admin
from taskit.infrastructure.cli.agenda import agenda


class State:
    def __init__(self,
                 admin_coordinator: AdminCoordinator,
                 agenda_coordinator: AgendaCoordinator):
        self.admin_coordinator = admin_coordinator
        self.agenda_coordinator = agenda_coordinator
        self.config = {"config": "taskit.conf"}


@click.group()
@click.pass_obj
def cli(obj):
    """Taskit CLI"""


cli.add_command(admin)
cli.add_command(agenda)
