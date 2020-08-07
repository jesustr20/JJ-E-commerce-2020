from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categorie'
        ordering = ['code']
    
    def __str__(self):
        return f'{self.name}'

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'

#almacen
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20, unique=True) #UNIQUE - PARA QUE NO SE PUEDA DUPLICAR EL CODIGO
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Products)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Store'
        ordering = ['name']
    
    def __str__(self):
        return f'{self.name}'

class Store_products(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.IntegerField(default=0)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Store_product'
        verbose_name_plural = 'Store_product'
        ordering = ['stock']
        unique_together = [['products','store']]
    
    def __str__(self):
        return f'{self.stock}'


#Modelos en linea
class Products_inline(admin.TabularInline):
    model = Products
    extra = 1

class Store_products_inline(admin.TabularInline):
    model = Store_products
    extra = 1
