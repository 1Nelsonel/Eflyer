from multiprocessing import context
from unicodedata import category
from django.shortcuts import redirect, render
from django.db.models import Q

from base.models import Category, Product, SubCategory

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = Product.objects.filter(
        Q(category__categoryName__icontains=q) |
        Q(productName__icontains=q) |
        Q(subCategory__subCategoryName__icontains=q) |
        Q(description__icontains=q) |
        Q(manufucturer__icontains=q) |
        Q(price__icontains=q) 

    )

    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    
    context = {'products': products, 'categories': categories, 'subcategories': subcategories, }
    return render(request, 'base/home.html', context)

def product(request, pk):
    product= Product.objects.get(id=pk)
    
    context ={'product': product}
    
    return render(request, 'base/product.html', context)

