from django.contrib import admin
from django.urls import path, include

from accounts import views
from django.contrib.auth.views import LogoutView
from .views import  ForgotPasswordView
from django.contrib.auth import views as auth_views






urlpatterns = [
    path('', views.login_user, name='user-login'),
    path('signup_moderator/', views.signup_moderator, name='signup-moderator'),
    path('logout/', LogoutView.as_view(next_page="main-page"), name="user-logout"),
    path('signup/', views.signup, name="user-create"),
    path('users/', views.main_page, name='main-page'),


    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]

