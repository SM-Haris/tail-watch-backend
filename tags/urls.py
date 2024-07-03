from django.urls import path, register_converter
from tags import views

urlpatterns = [
    path("", views.tag_list_create_view, name="tag-list-create"),
    path("<uuid:id>/", views.tag_detail_view, name="tag-detail"),
    path("<uuid:id>/update/", views.tag_update_view, name="tag-update"),
    path("<uuid:id>/delete/", views.tag_delete_view, name="tag-delete"),
]
