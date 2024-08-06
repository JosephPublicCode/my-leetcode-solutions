-- # Write your MySQL query statement below
Select round(100*sum(imm_bool)/count(customer_id),2) as immediate_percentage
From(
SELECT u.customer_id, u.order_date, d.customer_pref_delivery_date, 
        if(d.customer_pref_delivery_date = u.order_date, 1, 0) as imm_bool
FROM (SELECT customer_id, min(order_date) as order_date
    FROM Delivery
    GROUP BY customer_id) as u
LEFT JOIN Delivery d
ON d.order_date = u.order_date AND d.customer_id = u.customer_id) as b

--  improved iteration

Select round(100*sum(case when order_date = customer_pref_delivery_date
        then 1 else 0 end)/count(distinct customer_id),2) as immediate_percentage
FROM Delivery 
WHERE (customer_id,order_date) in (
SELECT customer_id, min(order_date) as order_date
FROM Delivery
GROUP BY customer_id)