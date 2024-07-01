from rest_framework import generics

from tags.mixins import UserQuerySetMixin
from tags.models import Tag
from tags.serializers import TagSerializer


class TagDetailAPIView(UserQuerySetMixin, generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = "pk"


class TagListCreateAPIView(UserQuerySetMixin, generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagUpdateAPIView(UserQuerySetMixin, generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDestroyAPIView(UserQuerySetMixin, generics.DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


tag_detail_view = TagDetailAPIView.as_view()
tag_list_create_view = TagListCreateAPIView.as_view()
tag_update_view = TagUpdateAPIView.as_view()
tag_delete_view = TagDestroyAPIView.as_view()
