"""
URL configuration for mysite project.

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

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),

    path('tpl', views.tpl),

    # news center
    path('news/', views.news),

    path('somethings/', views.somethings),

    # 案件：ユーザーログイン
    path('login/', views.login),

    path('orm/', views.orm),

    # ユーザー管理機能
    path('user/admin/', views.user_admin),
    path('user/add/', views.user_add),
    path('user/delete/', views.user_delete),
]
