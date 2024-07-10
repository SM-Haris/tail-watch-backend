from django.urls import path
from .views import history_create_view,history_list_view

urlpatterns = [
    path('', history_create_view, name='history-create'),
    path('<uuid:tag_id>/', history_list_view, name='history-list'),
]
