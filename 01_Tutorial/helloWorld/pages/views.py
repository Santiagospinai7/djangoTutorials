from django.shortcuts import render # here by default
from django.views.generic import TemplateView


class HomePageView(TemplateView):
  template_name = 'home.html'