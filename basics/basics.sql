SELECT COUNT(DISTINCT Price)
FROM Products;

SELECT COUNT(Products) AS [Number Of Products], CategoryId From Products GROUP BY CategoryId;

'''
SQL Joins
'''
SELECT Products.ProductID, Products.ProductName, Categories.CategoryName from Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

'''
If columns are present in both tables, then mention table names along with column name. If not, if columns are different in both table, just mentioning column name is enough.

'''

-- Aggregate Functions 

select s.name, count(m.subject) as subjects_count from students s JOIN marks m ON m.student_id = s.student_id group by s.name;

select s.name, sum(m.score) as sum_value from students s JOIN marks m ON m.student_id = s.student_id group by s.name HAVING sum(m.score) > 150;

select m.subject, avg(m.score) as AVG_SUM from students s JOIN marks m ON m.student_id = s.student_id GROUP BY m.subject ;

select s.name, sum(m.score) from students s JOIN marks m ON m.student_id = s.student_id group by s.name;

delete from marks where student_id = 4;

ALTER TABLE marks rename column score to total_score;

ALTER marks add column 'score';

select tweet_id from Tweets where length(content) > 15;

select name, population, area from World where area >= 3000000 or population >= 25000000;

select distinct(author_id) as id from Views where author_id = viewer_id;