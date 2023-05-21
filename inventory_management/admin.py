from django.contrib import admin
from .models import Product, Category, Supplier

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'qty_stock', 'price', 'category', 'image', 'bar_code']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'product']
