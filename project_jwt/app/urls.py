# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('criarUsuarios/', views.create_user, name='create_user'),
    path('logar/', views.logar, name='logar'),
    path('fazAlgumaCoisa/', views.view_protegida, name="view_protegida"),
]
