from django.shortcuts import render
from django.views.generic import View








class Index_views(View):

    def get(self, request):

        return render(request, 'initial/index.html')