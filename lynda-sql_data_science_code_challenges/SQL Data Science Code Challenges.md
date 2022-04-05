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









