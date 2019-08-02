"""MyLotoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.connexion,name='login'),
    path('myLogin',views.myLogin,name='myLogin'),
    path('myRegister',views.myRegister,name='myRegister'),
    path('scrap',views.scrap,name='scrap'),
    path('<int:math_id>/',views.parie,name='parie'),
    path('logout/',views.myLogout,name='logout'),
    path('compte/',views.compte,name='compte'),
    path('saveParie',views.saveParie,name='saveParie'),
    path('AtualisationParie/<int:>',views.AtualisationParie,name='AtualisationParie'),
]
