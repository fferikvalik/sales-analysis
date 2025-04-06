-- database/queries.sql
-- Топ-регионы по продажам
SELECT region, SUM(total) AS revenue
FROM sales
GROUP BY region
ORDER BY revenue DESC;
