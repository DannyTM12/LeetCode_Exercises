SELECT p.product_name, s.year, s.price --The trhee columns that the problems need
FROM Products p
INNER JOIN Sales s -- We do not have null data and we can use the inner join
    ON s.product_id = p.product_id