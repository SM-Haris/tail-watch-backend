from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from shared.mixins import AuditLogMixin
from tags.mixins import SuperuserSerializerMixin, UserQuerySetMixin
from tags.models import Tag
from tags.serializers import TagSerializer, TagTrackSerializer, TagUpdateSerializer
from rest_framework_bulk.generics import BulkCreateAPIView


class TagDetailAPIView(
    AuditLogMixin, UserQuerySetMixin, SuperuserSerializerMixin, generics.RetrieveAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "id"


class TagBulkCreateView(AuditLogMixin, SuperuserSerializerMixin, BulkCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_bulk_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagListCreateAPIView(
    AuditLogMixin,
    UserQuerySetMixin,
    SuperuserSerializerMixin,
    generics.ListCreateAPIView,
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
    AuditLogMixin, UserQuerySetMixin, SuperuserSerializerMixin, generics.UpdateAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagUpdateSerializer
    lookup_field = "id"


class TagDestroyAPIView(
    AuditLogMixin, UserQuerySetMixin, SuperuserSerializerMixin, generics.DestroyAPIView
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "id"

class TagTrackAPIView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagTrackSerializer
    lookup_field = 'id'
    permission_classes = []
    authentication_classes =[]


tag_detail_view = TagDetailAPIView.as_view()
tag_list_create_view = TagListCreateAPIView.as_view()
tag_bulk_create_view = TagBulkCreateView.as_view()
tag_update_view = TagUpdateAPIView.as_view()
tag_delete_view = TagDestroyAPIView.as_view()
tag_track_view = TagTrackAPIView.as_view()
