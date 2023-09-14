from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post, Category
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from blogging.serializers import PostSerializer, CategorySerializer, UserSerializer


class BloggingListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    context_object_name = "posts"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


class BloggingDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    context_object_name = "posts"
    queryset = Post.objects.exclude(published_date__exact=None)

    def get_post(self, queryset):
        if queryset is None:
            queryset = self.model._default_manager.exclude(published_date__exact=None)

        key = self.kwargs.get("post_id")
        try:
            return queryset.get(pk=key)
        except Post.DoesNotExist:
            raise Http404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """

    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Category to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
