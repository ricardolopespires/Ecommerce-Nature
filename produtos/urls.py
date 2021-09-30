from django.urls import path
from . import views
import produtos



app_name = 'produtos'


urlpatterns = [ 

     path('',views.List_Products.as_view(), name = 'list_products'),
     path('produtos/<slug:categoria_slug>/', views.List_Products.as_view(), name = 'produtos_list_da_categoria'),
     path('<slug:categoria_slug>/<slug:produto_slug>/',views.Product_Detail.as_view(), name = 'details'),
]

