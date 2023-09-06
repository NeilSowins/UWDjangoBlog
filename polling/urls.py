# polling/urls.py
from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path("", PollListView.as_view(), name="poll_index"),
    path("polls/<int:poll_id>/", PollDetailView.as_view(), name="poll_detail"),
]
