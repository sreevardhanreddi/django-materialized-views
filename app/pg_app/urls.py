from django.urls import path
from pg_app.views import (
    index,
    blogs,
    blogs_with_categories,
    blogs_with_categories_and_tags,
)


app_name = "app"

urlpatterns = [
    path("", index, name="index"),
    path("blogs/", blogs, name="blogs"),
    path("blogs-with-categories/", blogs_with_categories, name="blogs_with_categories"),
    path(
        "blogs-with-categories-and-tags/",
        blogs_with_categories_and_tags,
        name="blogs_with_categories_and_tags",
    ),
]
