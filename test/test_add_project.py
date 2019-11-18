from model.project import Project


def test_add_project(app):
    project = Project(name="Test_prj", status="development", description="Some_test_description",  public="public")
    old_projects = app.project.get_project_list()
    app.project.create(project)
    assert len(old_projects)+1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=project.id_or_max) == sorted(new_projects, key=project.id_or_max)