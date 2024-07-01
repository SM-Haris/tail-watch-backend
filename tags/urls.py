from django.urls import path
from . import views


urlpatterns = [
    path('',views.tag_list_create_view),
    path('<int:pk>',views.tag_detail_view),
    path('<int:pk>/update',views.tag_update_view),
    path('<int:pk>/delete',views.tag_delete_view),
]