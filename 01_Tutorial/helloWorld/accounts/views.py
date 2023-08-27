from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  return render(request, 'signup.html',{'form':UserCreationForm})

