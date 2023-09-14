from django.urls import path, include
from rest_framework import routers
from blogging.views import BloggingListView, BloggingDetailView, PostViewSet, CategoryViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'users', UserViewSet, basename='user-detail')


urlpatterns = [
    path("", BloggingListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BloggingDetailView.as_view(), name="blog_detail"),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
