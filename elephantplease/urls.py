"""
URL configuration for elephantplease project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home, name="home" ),
    path('rent/',views.rent, name="rent" ),
    path('lend/',views.lend, name="lend" ),
    path('search/',views.search, name="search" ),
    path('sign in/',views.sign_in, name="sign in" ),
    path('sign up/',views.sign_up, name="sign up" ),
    path('forget_password/',views.forget_password, name="forget_password" ),
    path('password_reset/',views.password_reset, name="password_reset" ),
    path('change_password/',views.change_password, name="change_password" ),
    path('hello/', include('core.urls')), 
]
