from django.contrib import admin
from django.urls import path
from site_ong import views

urlpatterns = [
    # o painel pronto do Django saiu de admin/ pra deixar esse link pra tela de login do site
    path('admin-django/', admin.site.urls),
    path('admin/', views.login_admin, name='login_admin'),
    path('admin/painel/', views.painel_admin, name='painel_admin'),
    path('', views.inicio, name='inicio'),
    path('sobre/', views.sobre, name='sobre'),
    path('projetos/', views.projetos, name='projetos'),
    path('doacao/', views.doacao, name='doacao'),
    path('voluntario/', views.voluntario, name='voluntario'),
]
