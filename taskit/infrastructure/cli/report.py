import click
from tabulate import tabulate


@click.group()
@click.pass_obj
def report(obj):
    """Taskit Report CLI"""


@report.command()
@click.option('--project_id', default="")
@click.pass_obj
def tasks(obj, project_id):
    if project_id:
       result = obj.state_reporter.list_tasks_in_project(project_id)
    else:
        result = obj.state_reporter.list_tasks()
    click.echo(tabulate(result, headers='keys'))


@report.command()
@click.pass_obj
def projects(obj):
    result = obj.state_reporter.list_projects()
    click.echo(tabulate(result, headers='keys'))
