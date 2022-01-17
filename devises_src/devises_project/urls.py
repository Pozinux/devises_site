"""DashboardDevise URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dashboard_app.views import dashboard, redirect_index

urlpatterns = [
    # on appelle la fonction redirect_index qui se trouve dans views.py quand on est sur la page d'accueil (donc chaine vide rajoutée à la suite de l'url)
    path("", redirect_index), 
    # on peut passer un int et une str comme une sorte de type de POST à la fonction dashboard
    # On donne un nom à l'url (ici home) pour pouvoir l'utiliser dans le template pour retrouver le chemin complet vers l'url
    path("days=<int:days_range>&currencies=<str:currencies>", dashboard, name='home'), 
    # url qui nous permet d'accèder à l'interface d'administration quand on met /admin à la suite de l'url
    path('admin/', admin.site.urls),
]