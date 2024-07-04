from django.urls import path
from .views import (
    tag_list_create_view,
    tag_bulk_create_view,
    tag_delete_view,
    tag_detail_view,
    tag_update_view,
)

urlpatterns = [
    path("", tag_list_create_view, name="tag-list-create"),
    path("bulk/", tag_bulk_create_view, name="tag-list-builk-create"),
    path("<uuid:id>/", tag_detail_view, name="tag-detail"),
    path("<uuid:id>/update/", tag_update_view, name="tag-update"),
    path("<uuid:id>/delete/", tag_delete_view, name="tag-delete"),
]
