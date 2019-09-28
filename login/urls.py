from rest_framework import routers
from login.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet, 'user')
