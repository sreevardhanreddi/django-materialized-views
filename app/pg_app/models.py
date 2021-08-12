from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        db_table = "tags"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tags)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        db_table = "blogs"

    def __str__(self):
        return self.title


class BlogsWithCategoriesAndTagsCombined(models.Model):
    id = models.IntegerField(primary_key=True)
    blog_title = models.CharField(max_length=200, unique=True)
    blog_content = models.TextField()
    blog_created_at = models.DateTimeField()
    blog_is_published = models.BooleanField()
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=200)
    tag_count = models.IntegerField()
    tags = models.JSONField()

    class Meta:
        managed = False
        db_table = "mv_blogs_with_categories_and_tags_combined"

    def __str__(self):
        return self.blog_title
