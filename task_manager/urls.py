"""task_manager URL Configuration
"""

from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet
from users.views import UserViewSet, UserRegister
from projects.views import ProjectViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/users/register/$', UserRegister.as_view()),
    url(r'^api/', include(router.urls)),
]
