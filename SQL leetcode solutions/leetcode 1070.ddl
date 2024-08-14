
-- leetcode 1070

-- Product Sales Analysis III


SELECT yt.product_id, first_year, quantity, price
FROM 
    (   
    SELECT product_id, min(year) AS first_year
    FROM Sales
    GROUP BY product_id) AS yt
JOIN Sales s
    ON yt.product_id = s.product_id AND yt.first_year = s.year


SELECT product_id, year AS first_year, quantity, price
FROM sales s
WHERE (product_id, year) 
        IN (
            SELECT product_id, min(year) 
            FROM sales 
            GROUP BY product_id)