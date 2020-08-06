from rest_framework import viewsets
from django.contrib.auth.models import User,Group, Permission
from .models import Categories, Products, Store, Store_products
from .serializers import (UserSerializer, 
                          GroupSerializer, 
                          PermissionSerializer,
                          CategoriesSerializer,
                          ProductsSerializer,
                          StoreSerializer,
                          Store_productsSerializer)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class Store_productsViewSet(viewsets.ModelViewSet):
    queryset = Store_products.objects.all()
    serializer_class = Store_productsSerializer