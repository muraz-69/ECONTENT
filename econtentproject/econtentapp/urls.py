from django.urls import path
from . import views

urlpatterns = [
    # Home Page (Main Landing Page) 
    path('', views.Home, name='home'),
    

    # Authentication
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'), 
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),

    # Bible & Man CRUD
    path('bible_and_man/', views.bible_and_man_list, name='bible_and_man_list'),
    path('bible_and_man/<int:pk>/', views.bible_and_man_detail, name='bible_and_man_detail'),
    path('bible_and_man/create/', views.bible_and_man_create, name='bible_and_man_create'),
    path('bible_and_man/<int:pk>/edit/', views.bible_and_man_update, name='bible_and_man_update'),
    path('bible_and_man/<int:pk>/delete/', views.bible_and_man_delete, name='bible_and_man_delete'),

    # Climate Change Awareness CRUD
    path('climate_change/', views.climate_change_list, name='climate_change_list'),
    path('climate_change/<int:pk>/', views.climate_change_detail, name='climate_change_detail'),
    path('climate_change/create/', views.climate_change_create, name='climate_change_create'),
    path('climate_change/<int:pk>/edit/', views.climate_change_update, name='climate_change_update'),
    path('climate_change/<int:pk>/delete/', views.climate_change_delete, name='climate_change_delete'),

    # Health & Wellness Resources CRUD
    path('health_wellness/', views.health_wellness_list, name='health_wellness_list'),
    path('health_wellness/<int:pk>/', views.health_wellness_detail, name='health_wellness_detail'),
    path('health_wellness/create/', views.health_wellness_create, name='health_wellness_create'),
    path('health_wellness/<int:pk>/edit/', views.health_wellness_update, name='health_wellness_update'),
    path('health_wellness/<int:pk>/delete/', views.health_wellness_delete, name='health_wellness_delete'),

    # Trendy Fashion & Apparel CRUD
    path('trendy_fashion/', views.trendy_fashion_list, name='trendy_fashion_list'),
    path('trendy_fashion/<int:pk>/', views.trendy_fashion_detail, name='trendy_fashion_detail'),
    path('trendy_fashion/create/', views.trendy_fashion_create, name='trendy_fashion_create'),
    path('trendy_fashion/<int:pk>/edit/', views.trendy_fashion_update, name='trendy_fashion_update'),
    path('trendy_fashion/<int:pk>/delete/', views.trendy_fashion_delete, name='trendy_fashion_delete'),

    # E-Books CRUD
    path('ebooks/', views.ebook_list, name='ebook_list'),
    path('ebooks/<int:pk>/', views.ebook_detail, name='ebook_detail'),
    path('ebooks/create/', views.ebook_create, name='ebook_create'),
    path('ebooks/<int:pk>/edit/', views.ebook_update, name='ebook_update'),
    path('ebooks/<int:pk>/delete/', views.ebook_delete, name='ebook_delete'),

    # Online Courses CRUD
    path('online_courses/', views.online_course_list, name='online_course_list'),
    path('online_courses/<int:pk>/', views.online_course_detail, name='online_course_detail'),
    path('online_courses/create/', views.online_course_create, name='online_course_create'),
    path('online_courses/<int:pk>/edit/', views.online_course_update, name='online_course_update'),
    path('online_courses/<int:pk>/delete/', views.online_course_delete, name='online_course_delete'),

    # Newsletter
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('manage-newsletters/', views.manage_subscriptions, name='manage_subscriptions'),
    path('edit-newsletter/', views.edit_newsletter, name='edit_newsletter'),
]
