# core/urls.py

from django.urls import path
from .views import ListaObjetosView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('lista/<str:modelo>/', ListaObjetosView.as_view(), name='lista_objetos'),
]
