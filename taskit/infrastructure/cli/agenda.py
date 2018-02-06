import click


@click.group()
@click.pass_obj
def agenda(obj):
    """Taskit Agenda CLI"""


@agenda.command()
@click.pass_obj
def new(obj):
    name = click.prompt("Please enter the task name", type=str)
    task_dict = {
        'name': name
    }
    obj.agenda_coordinator.create_task(task_dict)
