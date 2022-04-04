from django.contrib import admin
from . models import Product, Category, SubCategory

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("productName", "category","price","manufucturer")
    search_fields = ("productName__startswith", "manufucturer__startswith" )
    list_filter = ("productName", "category", "price","manufucturer" )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("categoryName", "created","updated")
    search_fields = ("categoryName__startswith", )
    list_filter = ("categoryName", )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("subCategoryName", "category", "created","updated")
    search_fields = ("subCategoryName__startswith",  )
    list_filter = ("subCategoryName","category", )

    

