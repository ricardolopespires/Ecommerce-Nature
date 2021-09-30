from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product, Review
from django.db.models import F, Sum, Q, Avg
from django.views.generic import View
from .forms import Review_Form

# Create your views here.





class List_Products(View):

    def get(self, request, categoria_slug = None):
        categorias = Category.objects.all()
        requested_categoria = None
        produtos = Product.objects.all()

        if categoria_slug:
            requested_categoria = get_object_or_404(Category, slug = categoria_slug)
            produtos = Product.objects.filter(category = requested_categoria)
        return render(request, 'produtos/list.html',{
            
            'categorias':categorias, 'produtos':produtos, 'requested_categoria':requested_categoria,
            
            
            })


class Product_Detail(View):

    def get(self, request, categoria_slug, produto_slug):
        categoria = get_object_or_404(Category, slug = categoria_slug)
        produto = get_object_or_404(Product, category_id = categoria.id, slug = produto_slug)
        reviews  = Review.objects.filter( produto_id = produto.id)
        reviews_avg = reviews.aggregate(Avg('rating'))['rating__avg']
        print(reviews_avg)

        if  request.method == 'POST':
            form = Review_Form(request.POST)
            if form.is_valid():
                cf = form.cleaned_data
                autor = "Anônimo"
                Review.objects.create(

                    produto = produto,
                    username = autor,
                    rating = cf['rating'],
                    texto = cf['texto']

                )
                return redirect(
                    
                    'produtos:details', categoria_slug = categoria_slug, produto_slug = produto_slug )
        else:
            form = Review_Form()

        return render(request, 'produtos/details.html',{'form':form,'produto':produto, 'reviews_avg':reviews_avg})



    def post(self, request, categoria_slug, produto_slug):
        categoria = get_object_or_404(Category, slug = categoria_slug)
        produto = get_object_or_404(Product, category_id = categoria.id, slug = produto_slug)
        reviews  = Review.objects.filter( produto_id = produto.id)
        reviews_avg = reviews.aggregate(Avg('rating'))['rating__avg']
        if  request.method == 'POST':
            form = Review_Form(request.POST)
            if form.is_valid():
                cf = form.cleaned_data
                autor = "Anônimo"
                Review.objects.create(

                    produto = produto,
                    username = autor,
                    rating = cf['rating'],
                    texto = cf['texto']

                )
                return redirect(
                    
                    'produtos:details', categoria_slug = categoria_slug, produto_slug = produto_slug)
        else:
            form = Review_Form()

        return render(request, 'produtos/details.html',{'form':form,'produto':produto})



    


