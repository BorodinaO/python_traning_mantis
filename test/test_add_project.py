from project_data.project_data import test_data
from model.project import Project
import pytest


@pytest.mark.parametrize("project", test_data, ids=[repr(x) for x in test_data])
def test_add_project(app, project):
    username = app.config['webadmin']['username']
    password = app.config['webadmin']['password']
    app.session.login(username, password)
    app.project.open_project_page()
    old_project_list = app.soap.get_project_all_list(username, password)
    app.project.create_project(project)
    new_project_list = app.soap.get_project_all_list(username, password)
    assert len(old_project_list) + 1 == len(new_project_list)
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
