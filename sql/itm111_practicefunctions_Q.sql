#--Use magazine DB--
#-------------Question 1 Below-------------------
#--List the magazine name and then take 3% off the magazine price and round to 2 decimal places.--
USE magazine;
SELECT magazineName, ROUND(magazinePrice - (magazinePrice * 0.03), 2) AS '3% off'
	FROM magazine;

#-------------Question 2 Below-------------------
#--Show the primary key of id from the subscriber table and using the date of 2020-12-20 as if it 
#--were today's date, how long in years, ROUNDED to the nearest year, has it been since their subscription started?--
USE magazine;
SELECT subscriberKey, ROUND(datediff('2020-12-20', subscriptionStartDate) / 365) AS 'Years since subscription'
	FROM subscription;

#-------------Question 3 Below-------------------
#--Show the subscriptionStartDate and subscriptionLength and add the  subscriptionLength to the 
#--subscriptionStartDate to see the date of how long their subscription will go. Format that date 
#--so it takes the format of Month name, number day with comma and then a 4 digit year.--
USE magazine;
SELECT subscriptionStartDate, subscriptionLength, date_format(date_add(subscriptionStartDate, INTERVAL subscriptionLength MONTH), '%M %e, %Y') AS 'subscription End'
	FROM subscription;

#--Use bike DB--
#-------------Question 4 Below-------------------
#--We need a list of all the products without the year at the end of the product_name string. 
#--Notice that some have two years listed, make sure you take those off as well. Order your results 
#--by product_id and limit your results to the first 14.--
USE bike;
SELECT REGEXP_REPLACE(product_name, ' - (\\d{4}(\\/\\d{4})*)$', '') AS 'Product Name Without Year'
	FROM product
    ORDER BY product_id
    LIMIT 14;

#-------------Question 5 Below-------------------
#--List the product name and then take the 2019 model year bikes and divide the price into 3 equal 
#--payments. Display one of the payments with a dollar sign, comma at the thousands place and two decimal places.--
USE bike;
SELECT product_name, CONCAT('$', FORMAT(list_price / 3, 2)) AS 'One of 3 payments'
	FROM product
    WHERE product_name LIKE '%2019'
    ORDER BY product_name;

