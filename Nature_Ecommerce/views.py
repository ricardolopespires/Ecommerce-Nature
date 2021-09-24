from django.shortcuts import render
from django.views.generic import View
from produtos.models import Category








class Index_views(View):

    def get(self, request):

        return render(request, 'initial/index.html')




class List_Products(View):

    def get(self, request):
        categorias = Category.objects.all()
        return render(request, 'initial/products.html',{'categorias':categorias})




