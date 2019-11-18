from model.project import Project
import random

def test_delete_some_group(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test_group"))
    old_projects = app.project.get_project_list()
    group = random.choice(old_projects)
    app.project.delete_project(group.id)
    new_projects = app.project.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects