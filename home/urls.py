from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("main_page/", views.mainpage, name='main_page'),
    path("signup/", views.signup, name='signup'),
    path("forgetpassword/", views.forgetpassword, name='forgetpassword'),
    path("otp_verify/", views.registration, name='otp_verify'),
    path("index/", views.otp_success, name='index'),
    path("reload/", views.re_load, name='reload'),
    path("userside/", views.userside, name='userside'),
    path("landingpage/", views.mainpage, name='main_page'),
    path("landingpage/", views.landingpage, name='landingpage'),
    path('forget/', views.forget, name='forget'),
    path('forget1/', views.forget1, name='forget1'),
    path('database/', views.database, name='database'),
    path('database/index', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('upload/index', views.index, name='index'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('resume/', views.upload_resume, name='resume'),
    path('demoupload/', views.demoupload, name='demoupload'),
    
]