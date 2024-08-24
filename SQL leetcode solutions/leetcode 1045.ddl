-- leetcode 1045 

-- Customer who bought all products

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(product_key)
    FROM Product);

