-- leetcode 1211

-- Queries Quality & percentage

-- First Attempt

SELECT query_name, 
        round(avg(quality),2) as quality,
        round(100*avg(poor_query_bool),2) as poor_query_percentage 
FROM (SELECT query_name, (rating/position) as quality, 
    if(rating < 3,1,0) as poor_query_bool
FROM Queries
WHERE query_name IS NOT NULL) as row_cals
GROUP BY query_name;

-- Improved Solution

SELECT query_name, 
    round(avg(rating/position), 2) as quality, 
    round(100*sum(rating < 3)/count(query_name),2) as poor_query_percentage
FROM queries
WHERE query_name IS NOT NULL
GROUP BY query_name; 