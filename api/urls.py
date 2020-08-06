from django.urls import path, include
from rest_framework import routers
from .viewsets import (UserViewSet, 
                       GroupViewSet, 
                       PermissionViewSet,
                       CategoriesViewSet,
                       ProductsViewSet,
                       StoreViewSet,
                       Store_productsViewSet)

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permisos',PermissionViewSet)
router.register(r'categorias',CategoriesViewSet)
router.register(r'productos',ProductsViewSet)
router.register(r'almacenes',StoreViewSet)
router.register(r'almacenes_productos',Store_productsViewSet)

urlpatterns = [
    path('',include(router.urls))
]