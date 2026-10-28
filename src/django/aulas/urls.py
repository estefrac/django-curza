from django.urls import path

from .views import (
    bye,
    cuarta_plantilla,
    edad,
    hello,
    primer_plantilla,
    segunda_plantilla,
    tercer_plantilla,
)

urlpatterns = [
    path("hello", hello),
    path("edad/<str:valor>/<str:futuro>", edad),
    path("bye", bye),
    path("plantilla", primer_plantilla),
    path("plantilla2", segunda_plantilla),
    path("plantilla3", tercer_plantilla),
    path("plantilla4", cuarta_plantilla),
]
