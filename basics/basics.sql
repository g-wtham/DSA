SELECT COUNT(DISTINCT Price)
FROM Products;

SELECT COUNT(Products) AS [Number Of Products], CategoryId From Products GROUP BY CategoryId;