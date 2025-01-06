from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PasswordResetViewSet


urlpatterns = [     
    path('password-reset/', PasswordResetViewSet.as_view(), name='password_reset'),      
        ]