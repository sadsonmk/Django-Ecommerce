from django.contrib import admin

from .models import Category,Product

admin.site.site_header = 'Kumix Store'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name','slug','created_at','updated_at']
  prepopulated_fields = {'slug' : ('name',)} 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title','author','slug','price','in_stock','created_at','updated_at']
  list_filter = ['in_stock','is_active']
  list_editable = ['price','in_stock']
  prepopulated_fields = {'slug' : ('title',)} 
