from rest_framework import generics
from .models import History
from .serializers import HistorySerializer, HistoryCreateSerializer


class HistoryCreateAPIView(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistoryCreateSerializer
    permission_classes = []
    authentication_classes = []


class HistoryListAPIView(generics.ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        tag_id = self.kwargs["tag_id"]
        return History.objects.filter(tag__id=tag_id)


history_create_view = HistoryCreateAPIView.as_view()
history_list_view = HistoryListAPIView.as_view()
