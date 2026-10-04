from django.urls import path
from .views import (RegisterView, MeView)
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path("login/",TokenObtainPairView.as_view(),name="login"),
    path("refresh/",TokenRefreshView.as_view(),name="refresh"),
    path("me/",MeView.as_view(),name="me"),
]
