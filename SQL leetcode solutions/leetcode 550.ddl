-- # leetcode 550

-- # Game Play Analysis IV

SELECT round(sum(result)/count(player_id),2) as fraction
FROM (
SELECT a.player_id, max(case when min_date = adddate(a.event_date,-1) then 1 else 0 end) as result
FROM (SELECT player_id, 
    min(event_date) as min_date
    FROM Activity
    GROUP BY player_id) as t
RIGHT JOIN Activity a
ON t.min_date = adddate(a.event_date,-1) and 
t.player_id = a.player_id
GROUP BY a.player_id) as b 


-- more efficient solution

SELECT
  ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
  Activity
WHERE
  (player_id, adddate(event_date,1))
  IN (
    SELECT player_id, MIN(event_date) AS min_date FROM Activity GROUP BY player_id
  )