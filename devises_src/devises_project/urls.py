"""devises_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path  # path est la fonction qui permet de créer un nouveau chemin d'URL

#from devises_src.dashboard_app.views import fonctionDeTest  # Sinon lorsque je lance le runserver j'ai l'erreur ModuleNotFoundError: No module named 'devises_src'
from dashboard_app.views import fonctionDeTest

urlpatterns = [
    path('admin/', admin.site.urls),  # url qui nous permet d'accèder à l'interface d'administration quand on met /admin à la suite
    path('fonctiondetest/', fonctionDeTest)
]
