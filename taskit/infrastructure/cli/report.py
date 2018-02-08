import click


@click.group()
@click.pass_obj
def report(obj):
    """Taskit Report CLI"""


@report.command()
@click.pass_obj
def tasks(obj):
    result = obj.state_reporter.list_tasks()
    for task_dict in result:
        click.echo(task_dict)


@report.command()
@click.pass_obj
def projects(obj):
    result = obj.state_reporter.list_projects()
    for project_dict in result:
        click.echo(project_dict)
