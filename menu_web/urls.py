"""menu_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from get_menu import views as gm
from main import views as ma

urlpatterns = [
    path('', ma.index, name='main'),
    path('admin/', admin.site.urls),
    path('updata/', gm.updata, name='update'),
    path('clean/', gm.clean, name='clean'),
    path('blog/<str:name>/', ma.blog, name='blog'),
    path('recommend/', ma.recommend, name='recommend'),
    path('search/', ma.search, name='search'),
    path('mail/', ma.mail, name='mail'),
    path('classify/', ma.classify, name='classify'),
]
