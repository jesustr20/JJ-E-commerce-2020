from django.urls import path, include
from rest_framework import routers
from .viewsets import UserViewSet, GroupViewSet, PermissionViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permisos',PermissionViewSet)

urlpatterns = [
    path('',include(router.urls))
]