from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from tags.mixins import SuperuserSerializerMixin, UserQuerySetMixin
from tags.models import Tag
from tags.serializers import TagSerializer, TagUpdateSerializer


class TagDetailAPIView(
    UserQuerySetMixin, SuperuserSerializerMixin, generics.RetrieveAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "id"


class TagListCreateAPIView(
    UserQuerySetMixin, SuperuserSerializerMixin, generics.ListCreateAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = [
        "gender",
        "subscription_choice",
    ]
    search_fields = ["pet_name", "disease", "recommended_medicine"]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagUpdateAPIView(
    UserQuerySetMixin, SuperuserSerializerMixin, generics.UpdateAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagUpdateSerializer
    lookup_field = "id"


class TagDestroyAPIView(
    UserQuerySetMixin, SuperuserSerializerMixin, generics.DestroyAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "id"


tag_detail_view = TagDetailAPIView.as_view()
tag_list_create_view = TagListCreateAPIView.as_view()
tag_update_view = TagUpdateAPIView.as_view()
tag_delete_view = TagDestroyAPIView.as_view()
