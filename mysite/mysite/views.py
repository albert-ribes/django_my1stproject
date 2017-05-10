from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.utils import timezone

def home(request):
    return render(request, 'mysite/home.html',)

