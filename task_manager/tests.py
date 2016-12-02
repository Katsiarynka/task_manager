from django.test import TestCase, Client
from users.models import Role, User, ROLE_DEVELOPER, ROLE_MANAGER


class BaseTests(TestCase, Client):

    @classmethod
    def setUpTestData(cls):
        super(BaseTests, cls).setUpTestData()
        cls.ajax = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
        cls.role_developer = Role.objects.create(name=ROLE_DEVELOPER)
        cls.role_manager = Role.objects.create(name=ROLE_MANAGER)

    @classmethod
    def create_user(cls, username='', email='', password='',  role=None, **kw):
        user = User(username=username, email=email, role=role, **kw)
        user.set_password(password)
        user.save()
        return user

    def authenticate(self, user):
        self.client.login(email=user.email, password=user.password)
