# Write your MySQL query statement below
SELECT *
FROM CINEMA
WHERE ID % 2 = 1 AND DESCRIPTION != "BORING"
ORDER BY RATING DESC;
