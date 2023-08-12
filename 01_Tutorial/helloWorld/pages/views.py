from django.shortcuts import render # here by default
from django.http import HttpResponse # new
from django.views.generic import TemplateView # new

# Create your views here.
# def homePageView(request): # new
#     return HttpResponse('Hello World!') # new

class HomePageView(TemplateView):
  template_name = 'pages/home.html'

class AboutPageView(TemplateView):
  template_name = 'pages/about.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
        "title": "About us - Online Store",
        "subtitle": "About us",
        "description": "This is an about page ...",
        "author": "Developed by: Santiago Ospina",
    })

    return context

class ContactPageView(TemplateView):
  template_name = 'pages/contact.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
        "title": "Contact us - Online Store",
        "subtitle": "Contact us",
        "email": "santiago@hotmail.com",
        "address": "1234 Main St",
        "phone": "132-456-7890",
    })

    return context
