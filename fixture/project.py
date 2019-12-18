from model.project import Project
import re


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/manage_proj_page.php"):
            return
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_css_selector("input[type='submit']").click()
        wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill contact form
        self.fill_form(project)
        # submit modification
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_project_page()
        self.project_cache = None

    def fill_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            project_tables = wd.find_element_by_css_selector(".width100[cellspacing='1']")
            project_list = project_tables.find_elements_by_xpath(".//tr[contains(@class, 'row')]")[1:]
            for i in project_list:
                name = i.find_elements_by_tag_name("td")[0].text
                descrpiption = i.find_elements_by_tag_name("td")[4].text
                self.project_cache.append(Project(name=name, description=descrpiption))
        return list(self.project_cache)

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        project_counter = len(wd.find_elements_by_xpath("//a[contains(@href, 'manage_proj_edit')]"))
        return project_counter
