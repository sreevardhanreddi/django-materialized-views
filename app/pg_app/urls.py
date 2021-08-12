from django.urls import path
from pg_app.views import (
    IndexPage,
    BlogsList,
    BlogsWithCategories,
    BlogsWithCategoriesAndTags,
    MaterializedBlogsWithCategoriesAndTags,
    BlogListAPIView,
    MaterializedBlogListAPIView,
)


app_name = "app"

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("blogs/", BlogsList.as_view(), name="blogs"),
    path(
        "blogs-with-categories/",
        BlogsWithCategories.as_view(),
        name="blogs_with_categories",
    ),
    path(
        "blogs-with-categories-and-tags/",
        BlogsWithCategoriesAndTags.as_view(),
        name="blogs_with_categories_and_tags",
    ),
    path(
        "materialized_blogs_with_categories_and_tags/",
        MaterializedBlogsWithCategoriesAndTags.as_view(),
        name="materialized_blogs_with_categories_and_tags",
    ),
    path(
        "api/blogs/",
        BlogListAPIView.as_view(),
        name="blog_list_api_view",
    ),
    path(
        "api/mat/blogs/",
        MaterializedBlogListAPIView.as_view(),
        name="materialized_blog_list_api_view",
    ),
]
