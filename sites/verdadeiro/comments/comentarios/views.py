from django.shortcuts import render
from . import models

# Create your views here.


def index(request):
    context = {'y': models.Perguntas.objects.all}
    return render(request, 'comentarios/index.html', context=context)
