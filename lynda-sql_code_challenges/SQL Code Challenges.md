# SQL Code Challenges

Link: https://www.linkedin.com/learning/sql-code-challenges/sql-code-challenges

Browser to use: [DB Browser for SQLite (sqlitebrowser.org)](https://sqlitebrowser.org/)



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

