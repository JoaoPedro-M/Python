from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request):
    context = {'lista_de_posts': Post.objects.all()}
    return render(request, 'blog/index.html', context=context)
