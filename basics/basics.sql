SELECT COUNT(DISTINCT Price)
FROM Products;

SELECT COUNT(Products) AS [Number Of Products], CategoryId From Products GROUP BY CategoryId;

'''
SQL Joins
'''
SELECT Products.ProductID, Products.ProductName, Categories.CategoryName from Products INNER JOIN Categories ON Products.CategoryID = Categories.CategoryID;

'''
If columns are present in both tables, then mention table names along with column name. If not, if columns are different in both table, just mentioning column name is enough.

