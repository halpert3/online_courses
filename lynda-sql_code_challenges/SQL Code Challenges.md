# SQL Code Challenges

Link: https://www.linkedin.com/learning/sql-code-challenges/sql-code-challenges

Browser to use: [DB Browser for SQLite (sqlitebrowser.org)](https://sqlitebrowser.org/)



## Order of an SQL query

```sql
SELECT DISTINCT column, AGG_FUNC(*column_or_expression*),… 
	FROM mytable    
	JOIN another_table      
		ON mytable.column = another_table.column    
	WHERE *constraint_expression*    
	GROUP BY column    
	HAVING *constraint_expression*    
	ORDER BY *column* ASC/DESC    
	LIMIT *count* OFFSET *COUNT*;
```



## Challenge 1

Create a list of all customers with:

* first name
* last name
* email

Sort it alphabetically by last name.

```sqlite
SELECT FirstName, LastName, Email 
FROM Customers
ORDER BY LastName ASC;
```



## Challenge 2

Create a table for RSVP's to the party with:

* CustomerID
* PartySize

```sqlite
CREATE TABLE AnniversaryAttendees (
	"CustomerID" INT,
	"PartySize" INT
);
```

*Don't forget you need to put "quotes" around the field names.*



## Challenge 3

Create 3 menus.

* All items sorted by price, low to high
* Appetizers and beverages by type (sorted by type)
* All items except beverages by type (sorted by type)

```sqlite
SELECT DishID, name, price, Type 
FROM Dishes
ORDER BY Price;

-- -- 

SELECT DishID, name, price, Type 
FROM Dishes
WHERE Type = "Appetizer" or Type = "Beverage"
ORDER BY Type;
-- --

SELECT DishID, name, price, Type 
FROM Dishes
WHERE Type IS NOT "Beverage"
ORDER BY Type;

-- OR

SELECT DishID, name, price, Type 
FROM Dishes
WHERE Type != "Beverage"
ORDER BY Type;
```



## Challenge 4

Insert a customer's info into the database. 

```sqlite
INSERT INTO Customers 
(FirstName, LastName, Email, Address, City, State, Phone, Birthday)
VALUES 
('John', 'Smith', 'jsmith@google.com', '44 Elm St.', 'New Orleans', 'LA', '504-444-5555', '1971-01-01')

```



## Challenge 5

Change customer's address.

* Taylor Jenkins in DC to 74 Pine St. New York, NY

  

```sqlite
SELECT * FROM Customers
WHERE FirstName LIKE "Tay%";

-- There are 2 Taylor Jenkins's. I want CustomerID 26

UPDATE Customers
SET Address = "74 Pine St.", City = "New York", State = "NY" 
WHERE CustomerID = 26;

```



## Challenge 6

Delete customer from database. Deleting customer with email "tjenkins@rouxacademy.org".



```sql
SELECT * FROM Customers
WHERE Email IS "tjenkins@rouxacademy.org";

-- There are 2 Taylor Jenkins's. I want CustomerID 4

DELETE FROM Customers WHERE CustomerID = 4;
```



## Challenge 7



Using the customer's email, find their ID and enter their party size in the AnniversaryAttendees table.

* Ashley with the email atapley2j@kinetecoinc.com is bringing 4 people 

```sql
INSERT INTO AnniversaryAttendees (CustomerID, PartySize)
VALUES( 
	(SELECT CustomerID FROM Customers WHERE Email = "atapley2j@kinetecoinc.com"),
	4); 
```

Notes:

* With sqlite, you need the VALUES keyword, which you may not need in other forms of SQL.
* After VALUES, parentheses are needed, and any SELECT statements need to be in parentheses, too.

**Git commit**

## Challenge 8

Search for a reservation by name without knowing the exact spelling.

"Stevenson" or something like it and four people in reservation. 

```sql
SELECT C.FirstName, C.LastName, R.ReservationID, R.Date  
FROM Customers AS C
JOIN Reservations AS R 
ON C.CustomerID = R.CustomerID
WHERE C.LastName like "Ste%"
	AND R.PartySize = 4;
```



This still gives you several reservations. But if you know today's date (which they didn't say in the video), you can find the right one. 

## Challenge 9

Create a reservation 

* Sam McAdams - 14 July 2020, 6 pm, 5 people
* smac@rouxacademy.com / (555) 555-1212



He's not already a customer so add him into the database.

```sql
INSERT INTO Customers (FirstName, LastName, Email, Phone)
VALUES ("Sam", "McAdams", "smac@rouxacademy.com", "(555) 555-1212");
```

Then add the reservation

```sql
INSERT INTO Reservations (CustomerID, Date, PartySize)
VALUES (
	(SELECT CustomerID FROM Customers WHERE Email = "smac@rouxacademy.com"),
	"2020-07-14 18:00:00",
	5
    );
```

It works, but when I double checked, I found the Reservation table wasn't set up with a primary key or to autoincrement it.  

**Git commit**

## Challenge 10

**Create order:**

- Loretta Hundey
- 6939 Elka Place
- Order:
  - House Salad,
  - Mini Cheeseburgers
  - Tropical Blue Smoothie

**Challenge**

- Create an order
- Find the customer
- Create the order record
- Add the items to the order
- Find the total cost 



Their way is confusing, so I'm changing up the sequence. 

### Find the customer

```sql
SELECT * FROM Customers
WHERE Address = "6939 Elka Place";
```

Her CustomerID is 70.

### Create the order

Does not auto-increment so I'm adding the ID as 1001. 

```sql
INSERT INTO Orders (OrderID, CustomerID, OrderDate)
VALUES (1001, 70, "2021-12-25 09:00:00");
```

### Add items to the order

```sql
SELECT DishID, Name, Price FROM Dishes
WHERE 
	Name = "House Salad" or 
	name = "Mini Cheeseburgers" or 
	name="Tropical Blue Smoothie";
```

You get IDs 4, 7, 20. 



Checking OrdersDishesID, it doesn't auto-increment and last one is 4021.

```sql
INSERT INTO OrdersDishes (OrdersDishesID, OrderID, DishID)
VALUES (4022, 1001, 4);
INSERT INTO OrdersDishes (OrdersDishesID, OrderID, DishID)
VALUES (4023, 1001, 7);
INSERT INTO OrdersDishes (OrdersDishesID, OrderID, DishID)
VALUES (4024, 1001, 20);
```

### Find the Cost

```sql
SELECT SUM(Dishes.Price) FROM Dishes
JOIN OrdersDishes 
ON Dishes.DishID = OrdersDishes.DishID
WHERE OrdersDishes.OrderID = 1001;
```



## Challenge 11

Update Cleo's favorite dish as the Quinoa Salmon Salad. (It's currently something else. Changing it from 14 to 9). 

```sql
UPDATE Customers
SET FavoriteDish = 
	(SELECT DishID FROM Dishes WHERE Name like "Quinoa%")
WHERE FirstName = "Cleo";
```





## Challenge 12

Generate a list of the five customers who have placed the most to-go orders.
