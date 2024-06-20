from django.shortcuts import render

#def jo(request):
#    return HttpResponse("Hello, Heroku!")

def accueil(request):
    return render(request, 'accueil.html')

def evenement(request):
    return render(request, 'evenements.html')

def panier(request):
    return render(request, 'panier.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


# Create your views here.
