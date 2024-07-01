from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer, CustomUserCreationSerializer
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


login_view = LoginView.as_view()
signup_view = SignupView.as_view()