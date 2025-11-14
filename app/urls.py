from django.urls import path
from . import views

urlpatterns = [
    path('timer/', views.contador_tempo_page, name='contador_tempo_page'),
    path('timer/status/', views.contador_tempo_status, name='contador_tempo_status'),
    path('timer/iniciar/', views.contador_tempo_iniciar, name='contador_tempo_iniciar'),
    path('timer/resetar/', views.contador_tempo_resetar, name='contador_tempo_resetar'),
]
