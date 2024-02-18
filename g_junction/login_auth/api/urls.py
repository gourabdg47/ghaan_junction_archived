from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import CustomTokenPairView
from . import views

urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),

    path('token/', CustomTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

