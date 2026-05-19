
SELECT COUNT(*) FROM api_data;

-- Average title length
SELECT AVG(title_length) FROM api_data;

-- Longest titles
SELECT title, title_length
FROM api_data
ORDER BY title_length DESC
LIMIT 5;

-- Posts per user
SELECT userid, COUNT(*) AS total_posts
FROM api_data
GROUP BY userid
ORDER BY total_posts DESC;