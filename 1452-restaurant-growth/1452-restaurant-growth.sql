# Write your MySQL query statement below
with daily as (
  select visited_on, sum(amount) as total_amount
  from customer
  group by visited_on
)
select a.visited_on, sum(b.total_amount) as amount, round(sum(b.total_amount)/7, 2) as average_amount
from daily a
join daily b on b.visited_on between date_sub(a.visited_on, interval 6 day) and a.visited_on
group by a.visited_on
having count(*) = 7
order by a.visited_on;
