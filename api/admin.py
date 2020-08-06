from django.contrib import admin
from .models import Categories, Products, Store, Store_products
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id','code','name','description','user']

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','code','name','description','user','categorie']

class StoreAdmin(admin.ModelAdmin):
    list_display = ['id','code','name','description','user']

class Store_productsAdmin(admin.ModelAdmin):
    list_display = ['id','stock','products','store']

admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Store_products,Store_productsAdmin)
