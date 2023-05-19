from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from myapp import views
import myapp
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.main,name="login"),
    path('home',views.home,name="home"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('about',views.about,name="about"),
    path('user',views.user,name="user"),
    path('viewprofile',views.viewprofile,name="viewprofile"),
    path('entrepreneur',views.entrepreneur,name="entrepreneur"),
    path('startupprofile',views.startupprofile,name="startupprofile"),
    path('usersettings',views.usersettings,name="usersettings"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('PostImage',views.PostImage,name="PostImage"),
    path('articles',views.articles,name="articles"),
    path('schemes',views.schemes,name="schemes"),
    path('startupsettings',views.startupsettings,name="startupsettings"),
    path('search',views.search,name="search"),
    path('otherprofile',views.otherprofile,name="otherprofile"),
    path('ouser',views.ouser,name="ouser"),
    path('userprofile',views.userprofile,name="userprofile"),
    path('suggestionbox',views.suggestionbox,name="suggestionbox"),
    path('startuplogo',views.startuplogo,name="startuplogo"),
    path('startupcp',views.startupcp,name="startupcp"),
    path('pitch',views.pitch,name="pitch"),
    path('entrepreneurdp',views.entrepreneurdp,name="entrepreneurdp"),
    path('entrepreneurcp',views.entrepreneurcp,name="entrepreneurcp"),
    path('entrepreneursettings',views.entrepreneursettings,name="entrepreneursettings"),
    path('entrepreneurprofile',views.entrepreneurprofile,name="entrepreneurprofile"),
    path('ostartupprofile',views.ostartupprofile,name="ostartupprofile"),
    path('oentrepreneurprofile',views.oentrepreneurprofile,name="oentrepreneurprofile"),
    path('form',views.form,name="form"),
    path('comment',views.comment,name ="comment")
] 
# app_name=myapp

