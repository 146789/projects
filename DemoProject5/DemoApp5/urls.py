from django.urls import path
from DemoApp5 import views
from django.contrib.auth import views as v
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('reg/', views.usrg, name="reg"),
    path('login/', v.LoginView.as_view(template_name='DemoApp5/login.html'), name="lg"),
    path('dashboard/', views.db, name="db"),
    path('logout/', v.LogoutView.as_view(template_name='DemoApp5/logout.html'), name='lo'),
    path('profile/', views.profile, name="profile"),
    path('update/', views.updated, name="upd")


    # path('login/', views.login, name="login")


]
