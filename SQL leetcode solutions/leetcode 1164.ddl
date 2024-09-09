-- leetcode 1164 

-- Product Price at a Given Date

--Join solution

SELECT distinct p.product_id, coalesce(t.new_price,10) as price
FROM products as p
LEFT JOIN(
    SELECT p.product_id, p.new_price
    FROM products as p
    JOIN (
        SELECT product_id, max(change_date) as cd
        FROM products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
        ) 
        as pi
    ON pi.product_id = p.product_id AND pi.cd = p.change_date
    ) as t 
ON t.product_id = p.product_id

-- Union Solution

SELECT product_id, new_price AS price
FROM products 
WHERE (product_id,change_date) IN (
    SELECT product_id, max(change_date) AS cd
    FROM products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION
SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN(
    SELECT DISTINCT product_id
    FROM product
    WHERE change_date <= '2019-08-16'
)
select distinct product_id, 10 as price from Products where product_id not in(select distinct product_id from Products where change_date <='2019-08-16' )
union 
select product_id, new_price as price from Products where (product_id,change_date) in (select product_id , max(change_date) as date from Products where change_date <='2019-08-16' group by product_id)

-- more efficient union solution

SELECT DISTINCT product_id, 10 AS price
FROM products
WHERE product_id NOT IN (
    SELECT DISTINCT product_id
    FROM products
    WHERE change_date <='2019-08-16'
)
UNION
SELECT product_id, new_price AS price
FROM products
WHERE (product_id, change_date) IN (
    SELECT product_id, max(change_date) AS date
    FROM products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
    )