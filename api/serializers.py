from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from .models import Categories, Products, Store, Store_products
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id','name','codename','content_type_id']


class GroupSerializer(serializers.ModelSerializer):
    #permissions = PermissionSerializer(many = True)
    class Meta:
        model = Group
        fields = ['id','name','permissions']

class UserSerializer(serializers.ModelSerializer):
        
    #groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['id','username','password','email','is_superuser','is_active','groups']

    #codigo crea el usuario y pide la contraseña y devuelve encriptada
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)
    

    #genera un token personal para cada uno automaticamente - solo para TokenAuthentication
    #@receiver(post_save, sender=settings.AUTH_USER_MODEL)
    #def create_auth_token(sender, instance=None, created=False, **kwargs):
    #    if created:
    #        Token.objects.create(user=instance)

class CategoriesSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = Categories
        fields = ['id','code','name','description','user']

class ProductsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    categorie = CategoriesSerializer()
    class Meta:
        model = Categories
        fields = ['id','code','name','description','user','categorie']

class StoreSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Store
        fields = ['id','code','name','description','user']

class Store_productsSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True)
    store = StoreSerializer(many=True)
    class Meta:
        model = Store_products
        fields = ['id','stock','products','store']