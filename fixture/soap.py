from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_all_list(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        project_list = client.service.mc_projects_get_user_accessible(username=username, password=password)
        projects = []
        for element in project_list:
            name = element.name
            status = element.status
            description = element.description
            id = element.id
            projects.append(Project(name=name, status=status, description=description, id=id))
        return list(projects)
