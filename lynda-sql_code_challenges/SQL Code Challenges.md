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

SELECT DishID, name, price, Type 
FROM Dishes
WHERE Type = "Appetizer" or Type = "Beverage"
ORDER BY Type;

SELECT DishID, name, price, Type 
FROM Dishes
WHERE Type IS NOT "Beverage"
ORDER BY Type;
```



