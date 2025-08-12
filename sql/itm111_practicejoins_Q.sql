#--Use v_art DB--
#-------------Question 1 Below-------------------
#--When you visit the Virtual Art Gallery Database Links to an external site. and you search by 
#--Period/Style and you choose Impressionism, you get two resulting images ("Woman in the Garden" 
#--and "Irises"). What query would be used in the code here to allow the user to see these images? 
#--No join is needed.--
USE v_art;
SELECT artfile
	FROM artwork
    WHERE period = 'Impressionism';

#-------------Question 2 Below-------------------
#--When you visit the Virtual Art Gallery Database Links to an external site., search by Subject 
#--and type in the word flower, you get three images. What query would have allowed the user to get 
#--those results (remember, the keyword might have been 'flowers' but they typed 'flower').--
USE v_art;
SELECT 
	a.artfile
FROM artwork a
JOIN artwork_keyword ak ON a.artwork_id = ak.artwork_id
JOIN keyword k ON ak.keyword_id = k.keyword_id
WHERE k.keyword LIKE '%flower%';

#-------------Question 3 Below-------------------
#--List all the artists from the artist table, but only the related artwork from the artwork table. 
#--We need the first name, last name, and artwork title.--
USE v_art;
SELECT 
	ar.fname, ar.lname, aw.title
FROM artist ar
LEFT JOIN artwork aw ON ar.artist_id = aw.artist_id;

#--Use magazine DB--
#-------------Question 4 Below-------------------
#--List all subscriptions with the magazine name, last name, first name, and sort alphabetically by magazine name.--
USE magazine;
SELECT 
	magazineName
    , subscriberLastName
    , subscriberFirstName
FROM subscription s1
LEFT JOIN magazine mag ON mag.magazineKey = s1.magazineKey
LEFT JOIN subscriber s2 ON s2.subscriberKey = s1.subscriberKey
ORDER BY magazineName;

#-------------Question 5 Below-------------------
#--List all the magazines that Samantha Sanders subscribes to.--
USE magazine;
SELECT 
	mag.magazineName
FROM subscription s1
LEFT JOIN magazine mag ON mag.magazineKey = s1.magazineKey
LEFT JOIN subscriber s2 ON s2.subscriberKey = s1.subscriberKey
WHERE s2.subscriberFirstName = 'Samantha'
	AND s2.subscriberLastName = 'Sanders'
ORDER BY magazineName;

#--Use employee DB--
#-------------Question 6 Below-------------------
#--List the first five employees from the Customer Service Department. Put them in alphabetical order by last name.--
USE employees;
SELECT
	e.first_name
    , e.last_name
FROM employees e
LEFT JOIN dept_emp de ON de.emp_no = e.emp_no
LEFT JOIN departments d ON d.dept_no = de.dept_no
WHERE d.dept_name = 'Customer Service'
ORDER BY e.last_name
LIMIT 5;

#-------------Question 7 Below-------------------
#--Find out the current salary and department of Berni Genin. You can use the ORDER BY and LIMIT to 
#--get just the most recent salary.--
USE employees;
SELECT
	e.first_name
    , e.last_name
    , d.dept_name
    , s.salary
    , s.from_date
FROM employees e
LEFT JOIN dept_emp de ON de.emp_no = e.emp_no
LEFT JOIN departments d ON d.dept_no = de.dept_no
LEFT JOIN salaries s ON s.emp_no = e.emp_no
WHERE e.first_name = 'Berni'
	AND e.last_name = 'Genin'
ORDER BY s.from_date DESC
LIMIT 1;