from django.shortcuts import render

#def jo(request):
#    return HttpResponse("Hello, Heroku!")

def accueil(request):
    return render(request, 'accueil.html')

def evenement(request):
    return render(request, 'evenements.html')


# Create your views here.
