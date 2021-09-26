from django.urls import path
from . import views



app_name = 'produtos'


urlpatterns = [ 

     path('produtos/',views.List_Products.as_view(), name = 'list_products'),
]