import click


@click.group()
@click.pass_obj
def admin(obj):
    """Taskit Admin CLI"""

####################
# New Commands Group
####################


@admin.group()
@click.pass_obj
def new(obj):
    """Taskit Admin New Commands Group"""


@new.command(name='project')
@click.pass_obj
def new_project(obj):
    name = click.prompt("Please enter the project name", type=str)
    project_dict = {
        'name': name
    }
    obj.admin_coordinator.create_project(project_dict)


#######################
# Update Commands Group
#######################

@admin.group()
@click.pass_obj
def update(obj):
    """Taskit Admin Update Commands Group"""


@update.command(name='project')
@click.pass_obj
def update_project(obj):
    uid = click.prompt("Please enter the project uid", default="")
    name = click.prompt("Please enter the project name", default="")
    comments = click.prompt("Please enter the project comments", default="")

    params = [('uid', uid), ('name', name), ('comments', comments)]
    # Ignore empty values in the project dictionary
    project_dict = dict(pair for pair in params if pair[1])

    obj.admin_coordinator.update_project(project_dict)


@update.command(name='task')
@click.pass_obj
def update_task(obj):
    uid = click.prompt("Please enter the task uid", default="")
    name = click.prompt("Please enter the task name", default="")
    due_date = click.prompt("Please enter the due date", default="")
    priority = click.prompt("Please enter the task priority", default="")
    stage = click.prompt("Please enter the task stage", default="")
    comments = click.prompt("Please enter the task comments", default="")

    params = [
        ('uid', uid), ('name', name), ('due_date', due_date),
        ('priority', priority), ('stage', stage), ('comments', comments)]
    # Ignore empty values in the project dictionary
    task_dict = dict(pair for pair in params if pair[1])

    obj.admin_coordinator.update_task(task_dict)


#######################
# Delete Commands Group
#######################

@admin.group()
@click.pass_obj
def delete(obj):
    """Taskit Admin Delete Commands Group"""


@delete.command(name='project')
@click.pass_obj
def delete_project(obj):
    uid = click.prompt("Please enter the project uid", default="")
    obj.admin_coordinator.delete_project(uid)


@delete.command(name='task')
@click.pass_obj
def delete_task(obj):
    uid = click.prompt("Please enter the task uid", default="")
    obj.admin_coordinator.delete_task(uid)
