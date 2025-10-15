-- This file is for documentation of Easy level questions from Analyst Builder
---------------------------------------------------------------------------
--                  Costco Rotisserie Loss
--Costco is known for their rotisserie chickens they sell, not just 
--because they are delicious, but because they are a loss leader in this area.
--This means they actually lose money in selling the chickens, but they 
--are okay with this because they make up for that in other areas.

--Using the sales table, calculate how much money they have lost on their 
--rotisserie chickens this year. Round to the nearest whole number.
SELECT 
    ROUND(SUM(lost_revenue_millions),0) AS 'Lost Money'
FROM sales;

---------------------------------------------------------------------------
--                  Perfect Data Analyst
--Return all the candidate IDs that have problem solving skills, SQL 
--experience, knows Python or R, and has domain knowledge.
--Order output on IDs from smallest to largest.
SELECT 
    candidate_id
FROM candidates
WHERE problem_solving = 'X'
    AND sql_experience = 'X'
    AND (python = 'X' OR r_programming = 'X')
    AND domain_knowledge = 'X'
ORDER BY candidate_id ASC;

---------------------------------------------------------------------------
--                  Car Failure
--Cars need to be inspected every year in order to pass inspection and be 
--street legal. If a car has any critical issues it will fail inspection 
--or if it has more than 3 minor issues it will also fail.

--Write a query to identify all of the cars that passed inspection.
--Output should include the owner name and vehicle name. Order by the 
--owner name alphabetically.
SELECT 
    owner_name,
    vehicle
FROM inspections
WHERE critical_issues = 0
    AND minor_issues <= 3
ORDER BY owner_name ASC;

---------------------------------------------------------------------------
--                  Electric Bike Replacement
--After about 10,000 miles, Electric bike batteries begin to degrade and 
--need to be replaced.

--Write a query to determine the amount of bikes that currently need to 
--be replaced. 

SELECT 
    COUNT(bike_id) AS 'Bikes that need new battery'
FROM bikes
WHERE miles > 10000;

---------------------------------------------------------------------------
--                  Sandwich Generation
--Yan is a sandwich enthusiast and is determined to try every combination 
--of sandwich possible. He wants to start with every combination of bread 
--and meats and then move on from there, but he wants to do it in a systematic way.

--Below we have 2 tables, bread and meats
--Output every possible combination of bread and meats to help Yan in his endeavors.
--Order by the bread and then meat alphabetically. This is what Yan prefers.
SELECT 
    bread_name
    , meat_name
FROM bread_table
CROSS JOIN meat_table
ORDER BY bread_name, meat_name;

---------------------------------------------------------------------------
--                  On The Way Out
--Herschel's Manufacturing Plant has hit some hard times with the economy 
--and unfortunately they need to let some people go.
--They figure the younger employees need their jobs more as they are 
--growing families so they decide to let go of their 3 oldest employees. 
--They have more experience and will be able to land on their feet easier 
--(and they had to pay them more).

--Write a query to identify the ids of the three oldest employees.
--Order output from oldest to youngest.
SELECT employee_id
FROM employees
ORDER BY birth_date ASC
LIMIT 3;

---------------------------------------------------------------------------
--                  Chocolate
--I love chocolate and only want delicious baked goods that have chocolate in them!

--Write a Query to return bakery items that contain the word "Chocolate".

SELECT product_name
FROM bakery_items
WHERE product_name LIKE '%Chocolate%';

---------------------------------------------------------------------------
--                  Million Dollar Store
--Write a query that returns all of the stores whose average yearly 
--revenue is greater than one million dollars.

--Output the store ID and average revenue. Round the average to 2 decimal places.
--Order by store ID. 
SELECT 
    store_id
    , ROUND(AVG(revenue),2) AS 'Average Revenue'
FROM stores
GROUP BY store_id
HAVING AVG(revenue) > 1000000
ORDER BY store_id;

---------------------------------------------------------------------------




---------------------------------------------------------------------------




---------------------------------------------------------------------------



---------------------------------------------------------------------------