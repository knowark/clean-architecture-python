import click


@click.group()
@click.pass_obj
def report(obj):
    """Taskit Report CLI"""


@report.command()
@click.pass_obj
def tasks(obj):
    obj.state_reporter.list_tasks()
