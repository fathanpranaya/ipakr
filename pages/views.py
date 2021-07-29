from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):
        # return JsonResponse({'status': 'oke'})
        return render(request, 'pages/home.html')
    # template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
