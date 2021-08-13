```sql

SELECT *
FROM blogs;


SELECT categories.id,
       categories.name
FROM categories;

--select categories.id, categories.name, count(catagories.id) from categories left join blogs on blogs.category_id = categories.id group by categories.id;
 --select categories.id, categories.name, blogs.id, blogs.title from categories left join blogs on blogs.category_id = categories.id;
 --select c.id, c.name, b.id, b.title from categories c left join blogs b on b.category_id = c.id;
 --select c.id, c.name, count(c.id) as blog_count, array_agg(b.id) as blog_ids from categories c left join blogs b on b.category_id = c.id group by c.id;
 -- query to get category id, name for a blog

SELECT b.id,
       b.title,
       b.category_id,
       c.id,
       c.name
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id ;

-- query to get blog tags

SELECT b.id,
       b.title,
       bt.blog_id,
       bt.tags_id
FROM blogs b
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id ;

-- query to count number of tags for a blog

SELECT b.id,
       b.title,
       bt.blog_id,
       count(bt.tags_id)
FROM blogs b
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
GROUP BY bt.blog_id,
         b.id;

-- query to count and get tag ids for a blog

SELECT b.id,
       b.title,
       bt.blog_id,
       count(bt.tags_id),
       array_agg(bt.tags_id)
FROM blogs b
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
GROUP BY bt.blog_id,
         b.id;


SELECT b.id,
       b.title,
       bt.blog_id,
       count(bt.tags_id),
       jsonb_agg(json_build_object('tag_id', bt.tags_id))
FROM blogs b
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
GROUP BY bt.blog_id,
         b.id;


SELECT b.id,
       b.title,
       c.id,
       c.name,
       bt.blog_id,
       bt.tags_id,
       t.id,
       t.name
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
LEFT JOIN tags t ON bt.tags_id = t.id;


SELECT b.id,
       b.title,
       c.id,
       c.name,
       bt.id,
       bt.blog_id,
       bt.tags_id,
       t.id,
       t.name
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
LEFT JOIN tags t ON bt.tags_id = t.id;


SELECT b.id AS blog_id,
       b.title AS blog_title,
       c.id AS category_id,
       c.name AS category_name,
       bt.blog_id AS blog_tag_blog_id,
       count(t.id),
       array_agg(t.id),
       array_agg(t.name)
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
LEFT JOIN tags t ON bt.tags_id = t.id
GROUP BY b.id,
         c.id,
         bt.blog_id ;


SELECT b.id AS blog_id,
       b.title AS blog_title,
       c.id AS category_id,
       c.name AS category_name,
       bt.blog_id AS blog_tag_blog_id,
       count(t.id),
       jsonb_agg(jsonb_build_object('tag_id', t.id, 'tag_name', t.name)) AS tag_json
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
LEFT JOIN tags t ON bt.tags_id = t.id
GROUP BY b.id,
         c.id,
         bt.blog_id ;


SELECT b.id,
       b.title AS blog_title,
       b.created_at AS blog_created_at,
       b.is_published AS blog_is_published,
       b.category_id AS blog_category_id,
       b.content AS blog_content,
       c.id AS category_id,
       c.name AS category_name,
       bt.blog_id AS blog_tag_blog_id,
       count(t.id) AS tag_count,
       jsonb_agg(jsonb_build_object('tag_id', t.id, 'tag_name', t.name)) AS tag_json
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
LEFT JOIN tags t ON bt.tags_id = t.id
GROUP BY b.id,
         c.id,
         bt.blog_id
ORDER BY b.id;


CREATE materialized VIEW mv_blogs_with_categories_and_tags_combined AS
SELECT b.id,
       b.title AS blog_title,
       b.content AS blog_content,
       b.created_at AS blog_created_at,
       b.is_published AS blog_is_published,
       c.id AS category_id,
       c.name AS category_name,
       count(t.id) AS tag_count,
       jsonb_agg(jsonb_build_object('tag_id', t.id, 'tag_name', t.name)) AS tags
FROM blogs b
LEFT JOIN categories c ON b.category_id = c.id
LEFT JOIN blogs_tags bt ON b.id = bt.blog_id
LEFT JOIN tags t ON bt.tags_id = t.id
GROUP BY b.id,
         c.id,
         bt.blog_id
ORDER BY b.id WITH NO DATA;


CREATE UNIQUE INDEX ON mv_blogs_with_categories_and_tags_combined (id);

REFRESH MATERIALIZED VIEW mv_blogs_with_categories_and_tags_combined;


SELECT *
FROM mv_blogs_with_categories_and_tags_combined;

REFRESH MATERIALIZED VIEW CONCURRENTLY mv_blogs_with_categories_and_tags_combined;


DROP materialized VIEW mv_blogs_with_categories_and_tags_combined;


SELECT *
FROM mv_blogs_with_categories_and_tags_combined;


```

```shell

python manage.py seed_mock_blogs_data

```

# Materialized Views for Faster Reads

seed mock data

```

python manage.py seed_mock_blogs_data

```

create an empty migration file

```python

python manage.py makemigrations --name materialized_blogs pg_app --empty

```
