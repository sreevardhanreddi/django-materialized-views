from django.shortcuts import render, HttpResponse
from pg_app.models import Blog

# Create your views here.
def index(request):
    return render(request, "index.html")


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, "blogs.html", {"blogs": blogs})


def blogs_with_categories(request):
    blogs = Blog.objects.select_related("category").all()
    # blogs = Blog.objects.all()
    return render(request, "blogs_with_categories.html", {"blogs": blogs})


def blogs_with_categories_and_tags(request):
    blogs = Blog.objects.select_related("category").prefetch_related("tags").all()
    # blogs = Blog.objects.all()
    return render(request, "blogs_with_categories_and_tags.html", {"blogs": blogs})
