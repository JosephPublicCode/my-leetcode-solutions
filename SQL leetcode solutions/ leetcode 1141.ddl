-- leetcode 1141

-- User Activity for the Past 30 Days I

SELECT activity_date as day, count(distinct user_id) as active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;

SELECT activity_date as day, count(distinct user_id) as active_users
FROM Activity
WHERE datediff('2019-07-27',activity_date) < 30 
GROUP BY activity_date;