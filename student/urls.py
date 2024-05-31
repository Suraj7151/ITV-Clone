"""
URL configuration for ItvedantProject project.

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
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.login_view),
    path('dashboard',v.home,name='dashboard'),
    path('profile',v.profile_view,name='profile'),
    path('interview-course',v.interview_view,name='interview'),
    path('aws-interview',v.aws,name='aws'),
    path('register',v.register_view,name='register'),
    path('login',v.login_view,name='login'),
    path('logout',v.logout_view,name='logout'),
    path('sql-study-material',v.sqlStudy,name='sqlContent'),
    path('wd-interview',v.wd,name='wdcontent'),
    path('search',v.searchView,name='intSearch'),
]
