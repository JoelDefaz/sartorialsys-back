from django.urls import path
from apps.users.api.api import UserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', UserAPIView.as_view(), name='users'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obtener el token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar el token
]
