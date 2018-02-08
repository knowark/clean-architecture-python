import click


@click.group()
@click.pass_obj
def agenda(obj):
    """Taskit Agenda CLI"""


@agenda.command()
@click.pass_obj
def new(obj):
    name = click.prompt("Please enter the task name", type=str)
    project_id = click.prompt("Please enter the project ID", type=str) 
    task_dict = {
        'name': name,
        'project_id': project_id
    }
    obj.agenda_coordinator.create_task(task_dict)


@agenda.command()
@click.pass_obj
def start(obj):
    uid = click.prompt("Please enter the task uid", type=str)
    obj.agenda_coordinator.start_task(uid)


@agenda.command()
@click.pass_obj
def complete(obj):
    uid = click.prompt("Please enter the task uid", type=str)
    obj.agenda_coordinator.complete_task(uid)
