-- # leetcode 596

-- # Classes more than 5 students

SELECT Class 
FROM (
SELECT Class, count(student) as st
FROM Courses 
GROUP BY Class) as g
WHERE st >= 5

SELECT Class
FROM Courses
GROUP BY Class
HAVING COUNT(student) >= 5