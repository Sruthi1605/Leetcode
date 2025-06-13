# Write your MySQL query statement below
select id, 
max(case when month='Jan' then revenue end) jan_revenue,
max(case when month='Feb' then revenue end) feb_revenue,
max(case when month='Mar' then revenue end) mar_revenue,
max(case when month='Apr' then revenue end) apr_revenue,
max(case when month='May' then revenue end) may_revenue,
max(case when month='Jun' then revenue end) jun_revenue,
max(case when month='Jul' then revenue end) jul_revenue,
max(case when month='Aug' then revenue end) aug_revenue,
max(case when month='Sep' then revenue end) sep_revenue,
max(case when month='Oct' then revenue end) oct_revenue,
max(case when month='Nov' then revenue end) nov_revenue,
max(case when month='Dec' then revenue end) dec_revenue
from department group by id;
