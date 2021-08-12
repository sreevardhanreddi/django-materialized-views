from django.shortcuts import render, HttpResponse
from pg_app.models import Blog, BlogsWithCategoriesAndTagsCombined
from django.views.generic import ListView, TemplateView


class IndexPage(TemplateView):
    template_name = "index.html"


class BlogsList(ListView):
    template_name = "blogs.html"
    queryset = Blog.objects.all()
    context_object_name = "blogs"


class BlogsWithCategories(ListView):
    template_name = "blogs_with_categories.html"
    queryset = Blog.objects.select_related("category").all()
    context_object_name = "blogs"


class BlogsWithCategoriesAndTags(ListView):
    template_name = "blogs_with_categories_and_tags.html"
    queryset = Blog.objects.select_related("category").prefetch_related("tags").all()
    context_object_name = "blogs"


class MaterializedBlogsWithCategoriesAndTags(ListView):
    template_name = "blogs_from_materialized_views.html"
    queryset = BlogsWithCategoriesAndTagsCombined.objects.all()
    context_object_name = "blogs"
