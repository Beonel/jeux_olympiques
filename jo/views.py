#from django.http import HttpResponse

#def jo(request):
#    return HttpResponse("Hello, Heroku!")
from django.shortcuts import render

def about(request):
    return render(request, 'accueil.html')


# Create your views here.
