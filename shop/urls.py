"""
URL configuration for MyAwsomeCart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    # path('',views.products,name="products"),
    # path('home/',views.index,name="index")
    path('',views.index,name="home"),
    path('collections/',views.collections,name="collections"),
    path('collectionsviews/<int:myid>',views.collectionsviews,name="collectionsviews"),
    path('checkout/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),
    path('aboutUs/',views.about,name="about"),
    path('signIn/',views.signIn,name="signIn"),
    path('signIn/loginUser/',views.loginUser,name="loginUser"),
    path("search/",views.search,name="search"),
    path("collectionsviews/prodView/<int:id>",views.prodView,name="prodView"),
]
