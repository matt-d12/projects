#--Start using bike DB--
#-------------Question 1 Below-------------------
#--Get the average quantity that we have in all our bike stocks. Round to the nearest whole number.--
USE bike;
SELECT
	FORMAT(AVG(quantity), 0) AS 'Stock Price'
FROM stock;

#-------------Question 2 Below-------------------
#--Show each bike that needs to be reordered. Filter the results to only the lowest quantity of 
#--zero. Order by product_name The image below show the first 12 of 24 rows total. You don't need 
#--to use a LIMIT.  (Hint for this one: Two different stores have the same bike that needs to be 
#--reordered. You only need it to show up once.)--
USE bike;
SELECT DISTINCT
	p.product_name
FROM product p
JOIN stock s ON p.product_id = s.product_id
WHERE s.quantity = 0
ORDER BY p.product_name;

#-------------Question 3 Below-------------------
#--How many of each category of bikes do we have in our "Baldwin Bikes" store, which has the 
#--store_id of 2. We need to see the name of the category as well as the number of bikes in the 
#--category. Sort it by lowest numbers first.--
USE bike;
SELECT
	c.category_name
    , SUM(s.quantity) AS 'instock'
FROM stock s
JOIN product p ON s.product_id = p.product_id
JOIN category c ON p.category_id = c.category_id
WHERE s.store_id = 2
GROUP BY c.category_name
ORDER BY instock;

#--Start using Employees DB--
#-------------Question 4 Below-------------------
#--How many employees do we have?--
USE employees;
SELECT 
	COUNT(*) AS 'Number of Employees'
FROM employees;

#-------------Question 5 Below-------------------
#--Get the average salaries in each department. We only need those departments that have average 
#--salaries that are below 60,000. Format the salary to 2 decimal places and a comma in the thousands place.--
USE employees;
SELECT
	d.dept_name
    , FORMAT(AVG(s.salary), 2)
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
JOIN salaries s ON e.emp_no = s.emp_no
GROUP BY d.dept_name
HAVING AVG(s.salary) < 60000;

#-------------Question 6 Below-------------------
#--Find out how many females work in each department. Sort by department name.--
USE employees;
SELECT
	d.dept_name
    , COUNT(e.emp_no) AS 'Number of Females'
FROM employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
WHERE e.gender = 'F'
GROUP BY d.dept_name
ORDER BY d.dept_name;
