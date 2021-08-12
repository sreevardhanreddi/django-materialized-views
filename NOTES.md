```sql

select * from blogs;

select categories.id, categories.name from categories;

--select categories.id, categories.name, count(catagories.id) from categories left join blogs on blogs.category_id = categories.id group by categories.id;

--select categories.id, categories.name, blogs.id, blogs.title from categories left join blogs on blogs.category_id = categories.id;

--select c.id, c.name, b.id, b.title from categories c left join blogs b on b.category_id = c.id;

--select c.id, c.name, count(c.id) as blog_count, array_agg(b.id) as blog_ids from categories c left join blogs b on b.category_id = c.id group by c.id;

-- query to get category id, name for a blog
select b.id, b.title, b.category_id , c.id , c.name from blogs b left join categories c on b.category_id = c.id ;

-- query to get blog tags
select b.id, b.title, bt.blog_id, bt.tags_id from blogs b left join blogs_tags bt on b.id = bt.blog_id ;

-- query to count number of tags for a blog
select b.id, b.title, bt.blog_id, count(bt.tags_id) from blogs b left join blogs_tags bt on b.id = bt.blog_id group by bt.blog_id , b.id;

-- query to count and get tag ids for a blog
select b.id, b.title, bt.blog_id, count(bt.tags_id), array_agg(bt.tags_id) from blogs b left join blogs_tags bt on b.id = bt.blog_id group by bt.blog_id, b.id;

select b.id, b.title, bt.blog_id, count(bt.tags_id), jsonb_agg(json_build_object('tag_id',bt.tags_id)) from blogs b left join blogs_tags bt on b.id = bt.blog_id group by bt.blog_id, b.id;

select b.id,
	b.title,
	c.id,
	c.name,
	bt.blog_id,
	bt.tags_id,
	t.id,
	t.name
from blogs b
left join categories c on b.category_id = c.id
left join blogs_tags bt on b.id = bt.blog_id
left join tags t on bt.tags_id = t.id;

select b.id,
	b.title,
	c.id,
	c.name,
	bt.id,
	bt.blog_id,
	bt.tags_id,
	t.id,
	t.name
from blogs b
left join categories c on b.category_id = c.id
left join blogs_tags bt on b.id = bt.blog_id
left join tags t on bt.tags_id = t.id;

select b.id as blog_id,
	b.title as blog_title,
	c.id as category_id,
	c.name as category_name,
	bt.blog_id as blog_tag_blog_id,
	count(t.id),
	array_agg(t.id),
	array_agg(t.name)
from blogs b
left join categories c on b.category_id = c.id
left join blogs_tags bt on b.id = bt.blog_id
left join tags t on bt.tags_id = t.id
group by b.id, c.id , bt.blog_id ;


select b.id as blog_id,
	b.title as blog_title,
	c.id as category_id,
	c.name as category_name,
	bt.blog_id as blog_tag_blog_id,
	count(t.id),
	jsonb_agg(jsonb_build_object('tag_id',t.id, 'tag_name',t.name)) as tag_json
from blogs b
left join categories c on b.category_id = c.id
left join blogs_tags bt on b.id = bt.blog_id
left join tags t on bt.tags_id = t.id
group by b.id, c.id , bt.blog_id ;


select b.id,
	b.title as blog_title,
	b.created_at as blog_created_at,
	b.is_published as blog_is_published,
	b.category_id as blog_category_id,
	b.content as blog_content,
	c.id as category_id,
	c.name as category_name,
	bt.blog_id as blog_tag_blog_id,
	count(t.id) as tag_count,
	jsonb_agg(jsonb_build_object('tag_id',t.id, 'tag_name',t.name)) as tag_json
from blogs b
left join categories c on b.category_id = c.id
left join blogs_tags bt on b.id = bt.blog_id
left join tags t on bt.tags_id = t.id
group by b.id, c.id , bt.blog_id order by b.id;


create materialized view all_tables
as
    select b.id,
        b.title as blog_title,
        b.content as blog_content,
        b.created_at as blog_created_at,
        b.is_published as blog_is_published,
        c.id as category_id,
        c.name as category_name,
        count(t.id) as tag_count,
        jsonb_agg(jsonb_build_object('tag_id',t.id, 'tag_name',t.name)) as tag
    from blogs b
    left join categories c on b.category_id = c.id
    left join blogs_tags bt on b.id = bt.blog_id
    left join tags t on bt.tags_id = t.id
    group by b.id, c.id , bt.blog_id order by b.id;

select * from all_tables;

drop materialized view all_tables ;

```

```shell

python manage.py seed_mock_blogs_data

```
