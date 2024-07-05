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
from .form import *
from django.contrib.auth import views as auth_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_v.LoginView.as_view(), name='login'),
    path('',v.login_view),
    path('dashboard',v.home,name='dashboard'),
    path('openingDetails/<int:cid>',v.openingDetail,name='openingDetail'),
    path('profile',v.profile_view,name='profile'),
    path('interview-course',v.interview_view,name='interview'),
    # path('aws-interview',v.aws,name='aws'),
    path('register',v.register_view,name='register'),
    path('login_view',v.login_view,name='login_view'),
    path('logout',v.logout_view,name='logout'),
    path('sql-study-material/<int:id>/',v.sqlStudy,name='sqlContent'),
    path('study-material/<int:id>/', v.study_material_view, name='study_material'),
    path('wd-interview/<int:id>/',v.wd,name='wdcontent'),
    path('search',v.searchView,name='intSearch'),
    # path('edit/<int:pk>',v.editProfile.as_view()),
    
    path('courses',v.course,name='course'),
    path('news',v.news,name='news'),
    path('news-search',v.news_search,name='newsSearch'),
    # path('cart',v.cart,name='cart'),
    path('addcart/<int:cid>/',v.add_to_cart,name='addcart'),
    path('cartlist',v.cart_list,name='cartlist'),
    # path('success',v.success_view,name='success'),

    path('update_cart/<int:item_id>/<str:action>/', v.update_cart, name='update_cart'),
    path('delete_from_cart/<int:item_id>/', v.delete_from_cart, name='delete_from_cart'),
    path('recognize_speech/', v.recognize_speech, name='recognize_speech'),



    path('courseSort/<str:category>/',v.sort,name='sort'),

    path('success/', v.payment_success, name='success'),
    

   path('password_reset/', auth_v.PasswordResetView.as_view(template_name='password_reset_form.html', success_url='/password_reset_done'), name='password_reset'),

    path('password_reset_done', auth_v.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',auth_v.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url='/password_reset_complete'), name='password_reset_confirm'),

    path('password_reset_complete', auth_v.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html',), name='password_reset_complete'),
]

