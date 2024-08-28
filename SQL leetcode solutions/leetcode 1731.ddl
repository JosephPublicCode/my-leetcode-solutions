-- leetcode 1731

-- The number of employees that report to each employee


-- # Write your MySQL query statement below
SELECT employee_id, name, reports_count, average_age
FROM Employees
RIGHT JOIN (
    SELECT reports_to as manager, count(reports_to) as reports_count, round(AVG(age)) as average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY manager) as r
ON r.manager = Employees.employee_id
ORDER BY employee_id