from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'index.html')


def administrador(request):
    return render(request,'administrador.html')
