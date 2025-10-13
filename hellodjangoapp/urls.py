"""
URL configuration for hellodjangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import homePageView
from .views import numbers_show
from .views import student_show
from .views import welcome
urlpatterns = [
    path('', homePageView, name ='home'),#new load-> http://127.0.0.1:8000/
    path('list/',numbers_show,name='numbers_show'),
    path('studentlist/',student_show, name='student_show'),
    path('welcome',welcome, name='welcome')
    
    
   
]
