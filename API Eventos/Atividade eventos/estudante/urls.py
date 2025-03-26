from django.urls import path
from . import views 

urlpatterns = [
    path('eventos/listar/', views.listar_eventos),
    path('eventos/criar/', views.criar_evento),
    path('eventos/<int:pk>/', views.detalhe_evento),
    path('eventos/alterar/<int:pk>/', views.alterar_evento),
    path('eventos/apagar/<int:pk>/', views.deletar_evento),
    path('eventos/proximos/', views.eventos_proximos),
]
