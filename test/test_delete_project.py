from model.project import Project
import random


def test_delete_some_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test_project", description="test_description"))
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project(project.name) # реализовать метод удаления проекта по имени
    new_projects = app.soap.get_project_list(username, password)
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects