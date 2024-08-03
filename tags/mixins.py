from admin_api.serializers import AdminTagSerializer

class UserQuerySetMixin:
    user_field = "owner"

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user

        queryset = super().get_queryset(*args, **kwargs)

        if self.request.user.is_superuser:
            return queryset

        return queryset.filter(**lookup_data)


class SuperuserSerializerMixin:
    admin_serializer_class = AdminTagSerializer

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return self.admin_serializer_class

        return self.serializer_class
