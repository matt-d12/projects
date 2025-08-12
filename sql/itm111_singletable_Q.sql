#-------------Question 1 Below-------------------
#--The manager wants to add the artist Johannes Vermeer as an artist in the database. He was born 
#--in 1632 and is from the Netherlands and died in 1674. He is not a local artist. What would the 
#--insert statement look like that would run as the manager adds a new artist to the system?--
USE v_art;
SELECT * FROM artist;
INSERT INTO artist VALUES
	(DEFAULT, 'Johannes', NULL, 'Vermeer', 1632, 1674, 'Netherlands', 'n');

#-------------Question 2 Below-------------------
#--If the manager lists all the artists with 'List all Artist Records' the following screen renders 
#--sorted by the last name of the artist. What query would allow all seven columns of values to 
#--show up on the screen alphabetically by the last name?--
USE v_art;
SELECT fname, mname, lname, dob, dod, country, local
	FROM artist
	ORDER BY lname;

#-------------Question 3 Below-------------------
#--The manager wants to edit Vermeer's information. She finds out that he died in 1675, not 1674. 
#--She selects EDIT next to Johannes Vermeer the following screen displays. The manager changes the 
#--'Date of Death' value to be 1675 and selects 'Update Entry'. What SQL statement will run in the 
#--background to accomplish this edit?--
USE v_art;
UPDATE artist
SET dod = 1675
	WHERE artist_id = 10;

#-------------Question 4 Below-------------------
#--The manager decides that she wants to delete Vermeer as an artist from her database. She selects 
#--the DELETE next to the Vermeer's row of information and the following screen renders confirming 
#--that she really wants to delete Vermeer as an artist. What SQL statement will run in the code 
#--that would delete Johannes Vermeer from the database when the manager selects 'Confirm Deletion'?--
USE v_art;
DELETE FROM artist
	WHERE artist_id = 10;

#--Use bike DB--
#-------------Question 5 Below-------------------
#--There is a product demonstration and bike race planned in Houston, Texas and you'd like to text 
#--each of your customers from that city to see if they will participate. You need a list of their 
#--first and last names and phone numbers.--
USE bike;
SELECT first_name, last_name, phone
    FROM customer
	WHERE phone IS NOT NULL AND city = 'Houston';

#-------------Question 6 Below-------------------
#--You need to sell more of your high-end bikes. You want to take $500 off all bikes that have a 
#--list price of $5,000.00 or more. You need to have a list showing the bike name, list price and 
#--discount price with an alias of 'Discount Price'. Sort the list showing the most expensive bike first.--
USE bike;
SELECT product_name, list_price, (list_price - 500) AS 'Discount Price'
	FROM product
    WHERE list_price >= 5000.00
    ORDER BY list_price DESC;

#-------------Question 7 Below-------------------
#--An important announcement was given to all the staff at your store (store_id 1). The same 
#--announcement needs to get to all the other staff at the other stores. You don't want to email 
#--all your staff again. You need a list of all the staff and their email who are not from your store.--
USE bike;
SELECT first_name, last_name, email
	FROM staff
    WHERE store_id != 1;

#-------------Question 8 Below-------------------
#--A customer needs more information about a specific bike, but all they know is that is has the 
#--word 'spider' in the name. You need to list the name, model year, and list price of all the bikes
#--with the word 'spider' somewhere in the name.--
USE bike;
SELECT product_name, model_year, list_price
	FROM product
    WHERE product_name LIKE '%spider%';

#-------------Question 9 Below-------------------
#--You need to list all bikes names that have a range of prices from $500–$550 sorted with the 
#--lowest price first.--
USE bike;
SELECT product_name, list_price
	FROM product
    WHERE list_price BETWEEN 500 AND 550
    ORDER BY list_price;

#-------------Question 10 Below-------------------
#--Show the customer's first_name, last_name, phone, street, city, state, zip_code who: have a phone
#--number listed and whose city has the letters 'ach' or 'och' somewhere in their name of the city
#--or whose last name is William. Limit the result set to the first five results.--
USE bike;
SELECT first_name, last_name, phone, street, city, state, zip_code
	FROM customer
    WHERE phone IS NOT NULL AND (city REGEXP 'ach|och' OR last_name = 'William')
    LIMIT 5;
