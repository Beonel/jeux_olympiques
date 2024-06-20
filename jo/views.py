from django.shortcuts import render

#def jo(request):
#    return HttpResponse("Hello, Heroku!")

def accueil(request):
    return render(request, 'accueil.html')


# Create your views here.
