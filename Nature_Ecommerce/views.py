from django.shortcuts import render
from django.views.generic import View
from produtos.models import Category








class Index_views(View):

    def get(self, request):

        return render(request, 'initial/index.html')



