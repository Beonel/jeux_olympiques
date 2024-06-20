from django.urls import path
from .views import jo, accueil

urlpatterns = [
    path('', jo, name='jo'),
    path('accueil/', accueil, name='accueil'),
]