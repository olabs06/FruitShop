from django.http import HttpResponse
from django.shortcuts import render
from .models import Veggie

# /products -> index
def index(request):
    veggies = Veggie.objects.all()
    return render(request, 'index.html', {'veggies':veggies})

    
def new(request):
    return HttpResponse('New Veggie')

