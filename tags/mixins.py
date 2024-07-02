from tags.serializers import TagAdminSerializer
from tags.utils import ExtractUserFromRequest


class UserQuerySetMixin:
    user_field = "owner"

    def get_queryset(self, *args, **kwargs):
        user = ExtractUserFromRequest(self.request)
        lookup_data = {}
        lookup_data[self.user_field] = user

        queryset = super().get_queryset(*args, **kwargs)

        if user.is_superuser:
            return queryset

        self.request.user = user
        return queryset.filter(**lookup_data)


class SuperuserSerializerMixin:
    admin_serializer_class = TagAdminSerializer

    def get_serializer_class(self):
        user = ExtractUserFromRequest(self.request)

        if user.is_superuser:
            return self.admin_serializer_class

        return self.serializer_class
