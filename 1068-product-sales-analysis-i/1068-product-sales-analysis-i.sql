# Write your MySQL query statement below

# pk: (sale_id, year)
# fk: product_id

select p.product_name, s.year, s.price
from sales s inner join product p
on s.product_id = p.product_id
;