# Write your MySQL query statement below
(select name as results from users u join (select user_id, count(*) as c from movierating group by user_id) r on u.user_id = r.user_id order by c desc, name limit 1)
union all
(select title as results from movies m join (select movie_id, avg(rating) as avg_rating from movierating where created_at between '2020-02-01' and '2020-02-29' group by movie_id) r on m.movie_id = r.movie_id order by avg_rating desc, title limit 1);
