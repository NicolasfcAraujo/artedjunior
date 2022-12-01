from django.shortcuts import render

# from utils.portifolio.factory import make_art

# Create your views here.


def home(request):
    return render(request, 'portifolio/home.html')
