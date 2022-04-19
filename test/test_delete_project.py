from model.project import Project
import random


def test_delete_some_project(app, db):
    if len(app.soap.get_projects()) == 0:
        app.project.create_project(Project(name='test', description='test'))
    old_projects = app.soap.get_projects()
    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    assert len(old_projects) - 1 == len(app.soap.get_projects())
    new_projects = app.soap.get_projects()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)