from django.urls import path
from .views import (
    admin_user_delete_view,
    admin_user_create_view,
    admin_user_detail_view,
    admin_user_list_view,
    admin_user_update_view
)

urlpatterns = [
    path("users/", admin_user_create_view, name="admin-user-create"),
    path("users/list/", admin_user_list_view, name="admin-user-list"),
    path("users/<uuid:id>/", admin_user_detail_view, name="admin-user-detail"),
    path("users/<uuid:id>/update/", admin_user_update_view, name="admin-user-update"),
    path("users/<uuid:id>/delete/", admin_user_delete_view, name="admin-user-delete"),
]
