from django.http import HttpResponse

def jo(request):
    return HttpResponse("Hello, Heroku!")

def accueil(request):
    return HttpResponse("Bienvenue sur la page d'accueil")


# Create your views here.
