from model.project import Project


def test_add_project(app, db, json_projects):
    project = json_projects
    old_projects = app.soap.get_projects()
    app.project.create_project(project)
    new_projects = app.soap.get_projects()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
