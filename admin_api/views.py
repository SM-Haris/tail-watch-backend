from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAdminUser
from shared.mixins import AuditLogMixin
from users.models import CustomUser
from .serializers import AdminUserSerializer
from rest_framework import generics


class AdminUserCreateAPIView(AuditLogMixin, generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]


class AdminUserUpdateAPIView(AuditLogMixin, generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    lookup_field= 'id'

class AdminUserRetrieveAPIView(AuditLogMixin,generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    lookup_field= 'id'

class AdminUserListAPIView(AuditLogMixin, generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["username", "email"]
    search_fields = ["username", "email", "address", "phone_number"]

class AdminUserDeleteAPIView(AuditLogMixin,generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]

admin_user_create_view = AdminUserCreateAPIView.as_view()
admin_user_list_view = AdminUserListAPIView.as_view()
admin_user_detail_view = AdminUserRetrieveAPIView.as_view()
admin_user_update_view = AdminUserUpdateAPIView.as_view()
admin_user_delete_view = AdminUserDeleteAPIView.as_view()