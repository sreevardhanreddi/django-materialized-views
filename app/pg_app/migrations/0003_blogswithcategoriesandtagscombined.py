# Generated by Django 3.2.6 on 2021-08-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg_app', '0002_materialized_blogs'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsWithCategoriesAndTagsCombined',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(max_length=200, unique=True)),
                ('blog_content', models.TextField()),
                ('blog_created_at', models.DateTimeField()),
                ('blog_is_published', models.BooleanField()),
                ('category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=200)),
                ('tag_count', models.IntegerField()),
                ('tags', models.JSONField()),
            ],
            options={
                'db_table': 'mv_blogs_with_categories_and_tags_combined',
                'managed': False,
            },
        ),
    ]
