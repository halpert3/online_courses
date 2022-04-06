# SQL Data Science Code Challenges

Link: https://www.linkedin.com/learning/sql-data-science-code-challenges

Database: Postgresql (downloaded on laptop) 

pgAdmin , Pass: I--v---3

# SQL Fundamentals

## Challenge 1

Find post insights info with the most recent ones first.

```sql
SELECT created_time, engaged_fans, post_clicks, reach, impressions
	FROM "PostInsights"
	ORDER BY created_time DESC

```



## Challenge 2

Find top countries with the highest number of fans.

Extract top 10 countries with their country code and number of fans from FansPerCountry table for the latest date, which is 2018-10-16

```sql
SELECT "CountryCode", "NumberOfFans"
	FROM "FansPerCountry"
	WHERE "Date" = '2018-10-16'
	ORDER BY "NumberOfFans" DESC
	LIMIT 10
;
```





## Challenge 3

Look at days where there's a greater number of average new likes in a day. Sorted order.

Group the data by date to extract the average number of new likes from GlobalPage 

![image-20220405164800984](C:\Users\halpe\AppData\Roaming\Typora\typora-user-images\image-20220405164800984.png)

```sql
SELECT DISTINCT date, NEW_LIKES
FROM "GlobalPage"
ORDER BY new_likes DESC
```

## Challenge 4

Group the data by date and determine the percentage of fans by gender from FansPerGenderAge

![image-20220405165603989](C:\Users\halpe\AppData\Roaming\Typora\typora-user-images\image-20220405165603989.png)

```sql
SELECT GENDER,
	SUM(NUMBER_OF_FANS),
	ROUND(SUM(NUMBER_OF_FANS) * 100 /
								(SELECT SUM(NUMBER_OF_FANS)
									FROM "FansPerGenderAge"
									WHERE date = '2018-10-16'),
		2) AS PERCENTAGE
FROM "FansPerGenderAge"
WHERE date = '2018-10-16'
GROUP BY GENDER
```

# SQL Joins

## Inner Joins

Find the top ten countries with highest penetration

- Penetration ratio is defined as number of fans/population
- Join FansPerCountry and PopStats tables on country code
- Extract data from latest date (2018-10-16)
- Order it and limit 10

```sql
SELECT DISTINCT P.COUNTRY_NAME,
	F."NumberOfFans",
	P.POPULATION,
	ROUND((F."NumberOfFans" * 100.0)/ P.POPULATION, 2) AS RATIO
FROM "PopStats" AS P
JOIN "FansPerCountry" AS F 
ON F."CountryCode" = P.COUNTRY_CODE
WHERE F."Date" = '2018-10-16'
ORDER BY RATIO DESC
LIMIT 10
```

## Outer and Cross Joins

Find bottom ten countries that have large populations but lowest number of fans

We're only looking at countries with 20,000,000 pop

- Join FansPerCountry and PopStats tables on country code
- Extract data from latest date (2018-10-16)
- Order by number of fans
- Only 10 rows

```sql
SELECT DISTINCT P.COUNTRY_NAME,
	F."NumberOfFans",
	P.POPULATION,
	ROUND((F."NumberOfFans" * 10000000.0) / P.POPULATION,
		2) AS RATIO
FROM "PopStats" AS P
JOIN "FansPerCountry" AS F 
ON F."CountryCode" = P.COUNTRY_CODE
WHERE F."Date" =
		(SELECT MAX("Date")
			FROM "FansPerCountry")
	AND P.POPULATION >= 20000000
ORDER BY F."NumberOfFans"
LIMIT 10
```

## Set theory for SQL Joins

Find the top cities and countries with highest number of fans

* Use JOIN to extract number of fans and country names
* Group by both city and country names 
* Order by number of fans after aggreration 
* Limit 10

```sql
SELECT CITY,
	COUNTRY_NAME,
	SUM(NUMBER_OF_FANS) AS TOTAL_FANS
FROM "FansPerCity" AS FPC
JOIN "PopStats" AS POP 
ON POP.COUNTRY_CODE = FPC.COUNTRY_CODE
GROUP BY city, country_name
ORDER BY TOTAL_FANS DESC
LIMIT 10
```

