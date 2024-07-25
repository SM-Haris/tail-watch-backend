from requests import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters,status
from rest_framework.response import Response
from shared.mixins import AuditLogMixin
from users.mixins import UserObjectMixin, UserQuerySetMixin
from .serializers import (
    CustomUserListSerializer,
    CustomUserUpdateSerializer,
    MyTokenObtainPairSerializer,
    CustomUserCreationSerializer,
    PasswordResetRequestSerializer,
    PasswordResetSerializer,
)
from rest_framework import generics
from .models import CustomUser


class LoginView(AuditLogMixin, UserQuerySetMixin, TokenObtainPairView):
    queryset = CustomUser.objects.all()
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = []
    authentication_classes = []


class SignupView(AuditLogMixin, UserQuerySetMixin, generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreationSerializer
    permission_classes = []
    authentication_classes = []

class UserUpdateAPIView(
    AuditLogMixin, UserObjectMixin, UserQuerySetMixin, generics.UpdateAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer


class UserListAPIView(AuditLogMixin, UserQuerySetMixin, generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password reset link has been sent to your email."}, status=status.HTTP_200_OK)


class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password has been reset successfully."}, status=status.HTTP_200_OK)


login_view = LoginView.as_view()
signup_view = SignupView.as_view()
custom_user_update_view = UserUpdateAPIView.as_view()
custom_user_detail_view = UserListAPIView.as_view()
password_reset_request_view = PasswordResetRequestView.as_view()
password_reset_confirm_view = PasswordResetConfirmView.as_view()