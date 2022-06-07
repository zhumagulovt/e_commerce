from django.contrib import admin

from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'created_at', 'updated_at')


admin.site.register(Category)