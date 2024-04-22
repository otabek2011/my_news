"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from news.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('detail/<int:id>/',detail, name='detail'),
    path('delete/<int:id>/', delete,name ="ochirish"),
    path('edit/<int:id>/', edit,name ="tahrirlash"),
    path('create_category/', createCategory, name='create_category'),
    path('user_register/', user_register, name='create_user'),
    path('user/edit/', user_edit, name="user_edit"),
    path('edit/form/<int:id>/',form_edit,name='edit_news_form'),
    path('password/edit/', password_edit, name='password_edit'),
    path('news/create/', createNews, name='create_news'),
    path("login/", Login, name='login'),
    path('logout/', Logout, name ='Logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

