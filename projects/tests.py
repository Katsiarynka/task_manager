from rest_framework.reverse import reverse
from task_manager.tests import BaseTests


class ProjectTest(BaseTests):

    def setUp(self):
        email = "%s@test.com"
        password = '12345'
        username = 'manager'
        role = self.role_manager
        self.manager = self.create_user(username, email % username, password, role)
        username = 'developer'
        role = self.role_developer
        self.developer = self.create_user(username, email % username, password, role)
        username = 'developer2'
        role = self.role_developer
        self.developer2 = self.create_user(username, email % username, password, role)

    def test_post(self):
        url = reverse('project-list')
        data = {"name": "Project1"}
        self.authenticate(self.manager)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 400)
        data["start"] = '2016-12-12'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], data["name"])
