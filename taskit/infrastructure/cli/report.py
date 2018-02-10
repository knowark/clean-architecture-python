import click
from tabulate import tabulate


@click.group()
@click.pass_obj
def report(obj):
    """Taskit Report CLI"""


@report.command()
@click.pass_obj
def tasks(obj):
    result = obj.state_reporter.list_tasks()
    click.echo(tabulate(result, headers='keys'))


@report.command()
@click.pass_obj
def projects(obj):
    result = obj.state_reporter.list_projects()
    click.echo(tabulate(result, headers='keys'))
