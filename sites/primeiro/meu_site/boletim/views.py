from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    context = {'materia': Materias.objects.all()}
    return render(request, 'boletim/index.html', context=context)
