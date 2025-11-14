from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('contadores/', views.listar_contadores, name='listar_contadores'),
    path('contadores/criar/', views.criar_contador, name='criar_contador'),
    path('contadores/<int:contador_id>/', views.ContadorView.as_view(), name='detalhe_contador'),
    path('contadores/<int:contador_id>/incrementar/', views.incrementar_contador, name='incrementar_contador'),
    path('estatisticas/', views.estatisticas, name='estatisticas'),
    path('operacao-demorada/', views.operacao_demorada, name='operacao_demorada'),
]

