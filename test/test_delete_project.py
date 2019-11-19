from random import randrange
from model.project import Project


def test_del_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    if len(app.project.get_project_list()) == 0:
        app.project.create_project(Project(name='Test', description="123"))
    old_project_list = app.project.get_project_list()
    index = randrange(len(old_project_list))
    app.project.delete_project_by_index(index)
    new_project_list = app.project.get_project_list()
    assert len(old_project_list) - 1 == len(new_project_list)
    del old_project_list[index]
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
