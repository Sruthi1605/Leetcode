# Write your MySQL query statement below
select product_id, product_name, description from products where description regexp '(^|[^a-zA-Z0-9])sn[0-9]{4}-[0-9]{4}([^0-9]|$)' order by product_id;
