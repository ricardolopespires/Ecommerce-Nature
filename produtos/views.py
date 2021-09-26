from django.shortcuts import render
from django.views.generic import View
from .models import Category, Product

# Create your views here.





class List_Products(View):

    def get(self, request):
        categorias = Category.objects.all()
        produtos = Product.objects.all()
        return render(request, 'initial/products.html',{'categorias':categorias, 'produtos':produtos, })




