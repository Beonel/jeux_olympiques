from django.urls import path
from .views import jo, accueil

urlpatterns = [
    path('', accueil, name='accueil'),
    path('jo/', jo, name='jo'),
]