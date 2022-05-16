"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path
from . import views

app_name = 'portfolio'
name = "home"

urlpatterns = [
    path('', views.home_page_view),
    path('home', views.home_page_view, name='home'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('projetos', views.projeto_page_view, name='projeto'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('nova/', views.nova_portfolio_view, name='nova'),
    path('edita/<int:portfolio_id>', views.edita_portfolio_view, name='edita'),
    path('apaga/<int:portfolio_id>', views.apaga_portfolio_view, name='apaga'),
]
