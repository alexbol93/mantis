from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] + "api/soap/mantisconnect.php?wsdl")
        project_list_soap = client.service.mc_projects_get_user_accessible(username, password)
        projects = []
        for element in project_list_soap:
            name = element.name
            description = element.description
            projects.append(Project(name=name, description=description))
        return projects

