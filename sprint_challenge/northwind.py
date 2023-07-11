import sqlite3

# Connect to the database
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# Execute the queries
expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

avg_hire_age = """
SELECT AVG(STRFTIME('%Y', HireDate) - STRFTIME('%Y', BirthDate)) 
AS Avg_Hire_Age
FROM Employee;
"""

ten_most_expensive = """
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10;
"""

largest_category = """
SELECT Category.CategoryName,
COUNT(DISTINCT Product.Id) AS unique_products_count
FROM Category
JOIN Product ON Category.Id = Product.CategoryId
GROUP BY Category.CategoryName
ORDER BY unique_products_count DESC
LIMIT 1;
"""

# Close the connection
conn.close()
