from django.contrib import admin
from . models import Category, Product

# Register your models here.



@admin.register(Category)
class Admin_Category(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Product)
class Admin_Product(admin.ModelAdmin):
    list_display = ['name','category','slug','price','available']
    list_filter = ['price','available']
    prepopulated_fields = {'slug':('name',)}

