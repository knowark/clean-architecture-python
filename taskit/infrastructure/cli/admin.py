import click


@click.group()
@click.pass_obj
def admin(obj):
    """Taskit Admin CLI"""
