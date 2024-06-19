from django.http import HttpResponse

def jo(request):
    return HttpResponse("Hello, Heroku!")

# Create your views here.
