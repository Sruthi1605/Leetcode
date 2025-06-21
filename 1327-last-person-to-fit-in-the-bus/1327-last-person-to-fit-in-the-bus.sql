# Write your MySQL query statement below
select person_name from (select *, sum(weight) over(order by turn) as total from queue) t where total <= 1000 order by total desc limit 1;
