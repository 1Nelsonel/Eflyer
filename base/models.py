from django.db import models
from django.contrib.auth.models import User

# Create your models for Category.
class Category(models.Model):
    categoryName = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.categoryName[0:50]

# Create your models for SubCategory.
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subCategoryName = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.subCategoryName[0:50]


# Create your models for Products.
class Product (models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    productName = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0)     
    productImage = models.ImageField(upload_to='uploads')
    manufucturer = models.CharField(max_length=200,default='Unidentified')
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.productName[0:50]

class Sales(models.Model):
    # buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    # price = 
    # dateSold =

    pass