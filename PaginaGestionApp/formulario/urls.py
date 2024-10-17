
from django.urls import path
from . import views

urlpatterns = [
    path('', views.formularioCliente, name="FormularioO"),
]
