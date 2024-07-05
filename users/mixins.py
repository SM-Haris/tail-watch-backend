class UserObjectMixin:

    def get_object(self):
        return self.request.user


class UserQuerySetMixin:

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user
        qs = queryset.filter(pk=user.id)
        return qs
