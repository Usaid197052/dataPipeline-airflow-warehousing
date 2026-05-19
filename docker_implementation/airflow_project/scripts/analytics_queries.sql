SELECT COUNT(*) FROM api_data;
SELECT AVG(title_length) FROM api_data;
SELECT title, title_length
FROM api_data
ORDER BY title_length DESC
LIMIT 5;
SELECT userid, COUNT(*) AS total_posts
FROM api_data
GROUP BY userid
ORDER BY total_posts DESC;