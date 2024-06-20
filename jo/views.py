from django.shortcuts import render
from django.contrib.auth.views import LoginView

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

def ajouter_au_panier(request):
    return render(request, 'ajouter_au_panier.html')

def supprimer_du_panier(request):
    return render(request, 'supprimer_du_panier.html')

def inscription(request):
    return render(request, 'inscription.html')

def connexion(request):
    return render(request, 'connexion.html')

def deconnexion(request):
    return render(request, 'deconnexion.html')

#Vue pour la connexion personnalisée
class CustomLoginView(LoginView):
    template_name = 'login.html'


# Create your views here.
