from pg_app.models import BlogsWithCategoriesAndTagsCombined
from django.db import connection


def refresh_materialized_blogs_views():
    cursor = connection.cursor()
    print("REFRESHING MATERIALIZED VIEW CONCURRENTLY ...")
    cursor.execute(
        """
        REFRESH MATERIALIZED VIEW CONCURRENTLY mv_blogs_with_categories_and_tags_combined;
        """
    )
    print("DONE.")
    return
