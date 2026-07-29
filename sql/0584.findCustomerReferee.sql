SELECT name -- Select only the name column
FROM Customers -- Search in the Customers table 
WHERE referee_id IS NULL OR referee_id != 2; -- Filter the results to include only customers who do not have a referee or whose referee is not customer 2