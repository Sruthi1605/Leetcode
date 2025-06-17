# Write your MySQL query statement below
select e.unique_id, emp.name from employees emp left join employeeuni e on emp.id = e.id;
