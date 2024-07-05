from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from shared.mixins import AuditLogMixin
from users.mixins import UserObjectMixin, UserQuerySetMixin
from .serializers import (
    CustomUserListSerializer,
    CustomUserUpdateSerializer,
    MyTokenObtainPairSerializer,
    CustomUserCreationSerializer,
)
from rest_framework import generics
from .models import CustomUser


class LoginView(AuditLogMixin, UserQuerySetMixin, TokenObtainPairView):
    queryset = CustomUser.objects.all()
    serializer_class = MyTokenObtainPairSerializer


class SignupView(AuditLogMixin, UserQuerySetMixin, generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreationSerializer


class UserUpdateAPIView(
    AuditLogMixin, UserObjectMixin, UserQuerySetMixin, generics.UpdateAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer


class UserListAPIView(AuditLogMixin, UserQuerySetMixin, generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]


login_view = LoginView.as_view()
signup_view = SignupView.as_view()
custom_user_update_view = UserUpdateAPIView.as_view()
custom_user_detail_view = UserListAPIView().as_view()
