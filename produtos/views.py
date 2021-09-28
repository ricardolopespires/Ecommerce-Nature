from django.shortcuts import get_object_or_404, render
from django.views.generic import View
from .models import Category, Product

# Create your views here.





class List_Products(View):

    def get(self, request, categoria_slug = None):
        categorias = Category.objects.all()
        requested_categoria = None
        produtos = Product.objects.all()

        if categoria_slug:
            requested_categoria = get_object_or_404(Category, slug = categoria_slug)
            produtos = Product.objects.filter(category = requested_categoria)
        return render(request, 'produtos/list.html',{'categorias':categorias, 'produtos':produtos, 'requested_categoria':requested_categoria })







