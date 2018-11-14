from django.urls import path

from .views import (
  BroadcastListView,
  BroadcastDetailView,
  TeacherDetailView,
)

urlpatterns = [
  path(
    "",
    BroadcastListView.as_view(),
    name='broadcast-list',
  ),
  path(
    "broadcast/<int:pk>",
    BroadcastDetailView.as_view(),
    name='broadcast-detail',
  ),
  path(
    "teacher/<int:pk>",
    TeacherDetailView.as_view(),
    name='teacher-detail',
  ),
]