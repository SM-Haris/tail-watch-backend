from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    login_view,
    signup_view,
    custom_user_update_view,
    custom_user_detail_view,
    password_reset_confirm_view,
    password_reset_request_view
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("update/", custom_user_update_view, name="user-update"),
    path("me/", custom_user_detail_view, name="user-list"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("password-reset/", password_reset_request_view, name="password-reset-request"),
    path("password-reset-confirm/", password_reset_confirm_view, name="password-reset-confirm"),
]
