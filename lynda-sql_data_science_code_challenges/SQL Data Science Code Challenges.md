# SQL Data Science Code Challenges

Link: https://www.linkedin.com/learning/sql-data-science-code-challenges

Database: Postgresql (downloaded on laptop) 

pgAdmin , Pass: I--v---3



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

