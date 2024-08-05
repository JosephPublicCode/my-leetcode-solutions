-- leetcode 1193 

-- Monthly Transactions I

SELECT substring(trans_date, 1, 7) as month, country, 
    count(state) as trans_count, 
    sum(if(state='approved',1,0)) as approved_count, 
    sum(amount) as trans_total_amount, 
    sum(if(state = 'approved',amount,0)) as approved_total_amount

FROM Transactions
GROUP BY month, country

-- improved solution