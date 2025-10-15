-- This file is for documentation of Moderate level questions from Analyst Builder
---------------------------------------------------------------------------
--                  TMI (Too Much Information)
--Often when you're working with customer information you'll want to sell 
--that data to a third party. Sometimes it is illegal to give away sensitive 
--information such as a full name.
--Here you are given a table that contains a customer ID and their full name.

--Return the customer ID with only the first name of each customer.
SELECT
    customer_id
    , SUBSTRING(full_name, 1, LOCATE(' ', full_name) - 1) AS first_name
    -- SUBSTRING: extract part of string starting at given position and for certain length
    -- Syntax: SUBSTRING(string, start_position, length)
    -- Length = LOCATE, go up to (but not include) the space at end of first name
FROM customers;

---------------------------------------------------------------------------
--                  Separation
--Data was input incorrectly into the database. The ID was combined with 
--the First Name.

--Write a query to separate the ID and First Name into two separate columns.
--Each ID is 5 characters long.
SELECT
    SUBSTRING(id, 1, 5) AS new_id
    , SUBSTRING(id, 6) AS first_name
FROM bad_data;
