from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', views.user_login, name='login'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('password_change/', auth_views.PasswordChangeView.as_view(),
         name="password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
    path('register/', views.register, name="register"),
    path('edit/', views.edit, name='edit')



]
# path('login/', v.LoginView.as_view(template_name='DemoApp5/login.html'), name="lg"),

# you change the template name usinh the above line

# Django also provides the authentication URL patterns that you just created. You can comment out the authentication URL patterns that you added to the urls.py file of the account application and include django.contrib.auth.urls instead, as follows:

# from django.urls import path, include
# # ...
# urlpatterns = [
#     # ...
#     path('', include('django.contrib.auth.urls')),
# ]