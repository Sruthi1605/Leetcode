# Write your MySQL query statement below
Select s.product_id, s.year as first_year, s.quantity, s.price from Sales s JOIN (SELECT product_id, MIN(year) as first_year from Sales group by product_id) as first_sale on s.product_id = first_sale.product_id and s.year = first_sale.first_year;
