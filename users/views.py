from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from users.mixins import UserObjectMixin, UserQuerySetMixin
from .serializers import (
    CustomUserListSerializer,
    CustomUserUpdateSerializer,
    MyTokenObtainPairSerializer,
    CustomUserCreationSerializer,
)
from rest_framework import generics
from .models import CustomUser


class LoginView(TokenObtainPairView):
    queryset = CustomUser.objects.all()
    serializer_class = MyTokenObtainPairSerializer
    permission_classes = []


class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreationSerializer
    permission_classes = []


class UserUpdateAPIView(UserObjectMixin, generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer


class UserListAPIView(UserQuerySetMixin, generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["username", "email"]
    search_fields = ["username", "email", "address", "phone_number"]


login_view = LoginView.as_view()
signup_view = SignupView.as_view()
custom_user_update_view = UserUpdateAPIView.as_view()
custom_user_list_view = UserListAPIView.as_view()
