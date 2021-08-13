from django.core.management.base import BaseCommand
from faker import Faker
from pg_app.models import Category, Tags, Blog
import random

fake = Faker()

categories = [fake.word() for i in range(100)]
tags = [fake.word() for i in range(100)]


class Command(BaseCommand):
    """
    create mock data for blogs
    """

    def _get_random_category(self):
        return random.choice(Category.objects.all())

    def _get_random_tags(self):
        return Tags.objects.order_by("?")[3 : random.randint(5, 10)]

    def _delete_previous_data(self):
        Blog.objects.filter().delete()
        Category.objects.filter().delete()
        Tags.objects.filter().delete()

    def create_tags(self):
        for tag in tags:
            Tags.objects.get_or_create(name=tag)

    def create_categories(self):
        for cat in categories:
            Category.objects.get_or_create(name=cat)

    def create_blogs(self):
        for i in range(1000):
            try:
                blog = Blog.objects.create(
                    title=fake.sentence(),
                    content=fake.paragraph(nb_sentences=50),
                    category=self._get_random_category(),
                )
                blog.tags.add(*self._get_random_tags())
            except Exception as e:
                print(e)

    def handle(self, *args, **options):
        # self._delete_previous_data()
        print("seeding mock data ...")
        self.create_tags()
        self.create_categories()
        self.create_blogs()
        print("Data created.")
