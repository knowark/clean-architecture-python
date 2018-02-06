import click


@click.group()
@click.pass_obj
def agenda(obj):
    """Taskit Agenda CLI"""


@agenda.command()
@click.pass_obj
def new(obj):
    print("TWO --->>", obj.config)
    click.echo('Running NEW Task')
    task_dict = {}
    obj.agenda_coordinator.create_task(task_dict)
    click.echo('Exiting NEW Task')
