from django.shortcuts import render


# Create your views here.


def index(request):
    context = {'id': 'aaaaaa'}
    return render(request, 'blogues/index.html', context=context)
