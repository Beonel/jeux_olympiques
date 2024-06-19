from django.urls import path
from .views import jo

urlpatterns = [
    path('', jo, name='home'),
]