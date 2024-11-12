from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('user', UserView, basename='user')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),           
    path('register/', RegisterView.as_view(), name='register'),           
    path('token/', TokenObtainPairView.as_view(), name='get_token'),           
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),           
    # path('home/', ProtectedView.as_view(), name='home'),           
        ] + router.urls
