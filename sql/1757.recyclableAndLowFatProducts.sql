SELECT product_id --Select only the product_id column
FROM Products -- Search in the Products table 
WHERE low_fat = 'Y' AND recyclable = 'Y'; -- Filter the results to include only products that are both low fat and recyclable