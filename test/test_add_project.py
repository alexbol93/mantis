from model.project import Project
from operator import attrgetter
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = Project(name=random_string("Project_name", 10), description=random_string("Project_description", 50))
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    app.project.create(project)
    assert len(old_projects)+1 == app.project.count()
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=attrgetter('name')) == sorted(new_projects, key=attrgetter('name'))
