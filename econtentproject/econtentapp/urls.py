from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'), 
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
    path('', views.bible_and_man_list, name='bible_and_man_list'),
    path('<int:pk>/', views.bible_and_man_detail, name='bible_and_man_detail'),
    path('create/', views.bible_and_man_create, name='bible_and_man_create'),
    path('<int:pk>/edit/', views.bible_and_man_update, name='bible_and_man_update'),
    path('<int:pk>/delete/', views.bible_and_man_delete, name='bible_and_man_delete'),
]
