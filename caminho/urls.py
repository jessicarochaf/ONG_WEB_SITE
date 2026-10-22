from django.contrib import admin
from django.urls import path
from site_ong import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('doacao/', views.doacao, name='doacao'),
    path('voluntario/', views.voluntario, name='voluntario'),
]
