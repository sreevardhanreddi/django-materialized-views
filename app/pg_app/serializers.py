from rest_framework import serializers
from pg_app.models import Blog, Category, Tags, BlogsWithCategoriesAndTagsCombined


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        id = ["id", "name"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        id = ["id", "name"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "is_published",
            "category",
            "tags",
        ]


class BlogsWithCategoriesAndTagsCombinedSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogsWithCategoriesAndTagsCombined
        fields = [
            "id",
            "blog_title",
            "blog_content",
            "blog_created_at",
            "blog_is_published",
            "category_id",
            "category_name",
            "tag_count",
            "tags",
        ]
