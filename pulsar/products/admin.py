from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'price', 'status', 'image')
    list_filter = ('status', )
    search_fields = ('name', 'code')
    list_per_page = 25
