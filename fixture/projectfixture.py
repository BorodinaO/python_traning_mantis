from model.project import Project
from selenium.webdriver.support.select import Select


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Manage Configuration'])[1]/following::input[2]").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text("release")
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::input[1]").click()
        wd.implicitly_wait(5)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']")[index].click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project_list = []
        for prj in wd.find_elements_by_css_selector("td > a[href*='manage_proj_edit_page.php?project_id']"):
            id = prj.get_attribute('search').split('=')[1]
            name = prj.text
            project_list.append(Project(name=name, id=id))
        return project_list
