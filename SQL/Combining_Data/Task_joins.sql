/* 
  TASK :
  Using SalesDB, Retrieve a list of all orders, along with the related customer,
  product and employee details.
  For Each Order Display :
  Order ID, customer's name, product name, sales, price, Sales person's name
*/
use SalesDB

-- Try to look after all the Tables and find the foreign keys and primary keys for joining.
--SELECT * FROM Sales.Customers
--SELECT * FROM Sales.Employees
--SELECT * FROM Sales.Orders
--SELECT * FROM Sales.OrdersArchive
--SELECT * FROM Sales.Products

SELECT 
	o.OrderID,
	/*CONCAT_WS lets us combine two column values with the separator specifier
	  - If there is only first_name and last_name is NULL or vice-versa
	   • In Normal String Concatenation like f_name + l_name it turns result to NULL
	   • In database logic, adding anything to a NULL always results in a completely blank NULL.
	  - We have 2 options to Combine 
	  1. CONCAT() - This will combine 2 string column but the separator will be added to first name if last name is null
	                CONCAT(f_name + ' ' + l_name) --> fname_ (if there is only f_name we see extra trailing sapce at end)
	  2. CONCAT_WS() - This will smartly combine the two string columns, it asks for separator to be passed as argument.
	                   CONCAT_WS(separator,col_1,col_2) -> CONCAT(' ',f_name,l_name)
					   even if any of column is NULL it shows the column with value but dont add the separator to the value.
	*/
	CONCAT_WS(' ',c.FirstName,c.LastName) AS Customer_name,
	p.Product AS Product_Name,
	o.sales,
	p.price,
	CONCAT_WS(' ',s.FirstName,s.LastName) AS Sales_Person
FROM Sales.Orders AS o
LEFT JOIN Sales.Customers AS c ON o.CustomerID = c.CustomerID
LEFT JOIN Sales.Products AS p ON o.ProductID = p.ProductID
LEFT JOIN Sales.Employees AS s ON o.SalesPersonID = s.EmployeeID
