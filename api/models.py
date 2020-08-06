from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
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
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categories,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
        ordering = ['code']
    
    def __str__(self):
        return f'{self.name}'

#almacen
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Store'
        ordering = ['code']
    
    def __str__(self):
        return f'{self.name}'

class Store_products(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.IntegerField(default=0)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    store = models.ForeignKey(Store,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Store_product'
        verbose_name_plural = 'Store_product'
        ordering = ['stock']
    
    def __str__(self):
        return f'{self.stock}'