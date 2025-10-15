--Given a table of candidates and their skills, you're tasked with finding 
--the candidates best suited for an open Data Science job. You want to find 
--candidates who are proficient in Python, Tableau, and PostgreSQL.
--Write a query to list the candidates who possess all of the required 
--skills for the job. Sort the output by candidate ID in ascending order.
SELECT candidate_id
FROM candidates
WHERE
  skill IN ('Python', 'Tableau', 'PostgreSQL')
  --Filter out rows with skills other than required ones
GROUP BY candidate_id
HAVING COUNT(skill) = 3
  --Filter only candidates with exactly all 3 skills
ORDER BY candidate_id ASC;

--------------------------------------------------------------------------
--Assume you're given two tables containing data about Facebook Pages and 
--their respective likes (as in "Like a Facebook Page").
--Write a query to return the IDs of the Facebook pages that have zero 
--likes. The output should be sorted in ascending order based on the page IDs.
SELECT p.page_id
FROM pages p
LEFT JOIN page_likes pl ON pl.page_id = p.page_id
GROUP BY p.page_id
HAVING COUNT(pl.user_id) = 0
ORDER BY p.page_id ASC;

--------------------------------------------------------------------------
