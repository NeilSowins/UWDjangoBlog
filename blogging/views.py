from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from blogging.models import Post
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BloggingListView(ListView):
    model = Post
    template_name = 'blogging/list.html'
    context_object_name = 'posts'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')


class BloggingDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    context_object_name = 'posts'
    queryset = Post.objects.exclude(published_date__exact=None)

    def get_post(self, queryset):
        if queryset is None:
            queryset = self.model._default_manager.exclude(published_date__exact=None)
        
        key = self.kwargs.get('post_id')
        try:
            return queryset.get(pk=key)
        except Post.DoesNotExist:
            raise Http404
