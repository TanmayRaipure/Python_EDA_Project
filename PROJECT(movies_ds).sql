CREATE DATABASE movielens;
USE movielens;

CREATE TABLE movies(
movieID INT PRIMARY KEY,
title VARCHAR(250),
genres VARCHAR(250)
);

CREATE TABLE users(
userID INT PRIMARY KEY,
gender CHAR(1),
age INT,
occupation INT,
zipcode VARCHAR(20)
);

CREATE TABLE ratings(
userID INT,
movieID INT,
rating FLOAT,
timestamp BIGINT,
FOREIGN KEY (userID) REFERENCES users(userID),
FOREIGN KEY (movieID) REFERENCES movies(movieID)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/movies.csv'
INTO TABLE movies
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
IGNORE 1 LINES
(movieId, title, genres);


LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/users.csv'
INTO TABLE users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
IGNORE 1 LINES
(userId, gender, age, occupation, zipcode);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 9.2/Uploads/ratings.csv'
INTO TABLE ratings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
IGNORE 1 LINES
(userId, movieId, rating, timestamp);

			
									-- TASKS-- 
-- 1. Top-rated genres by age group-- 

SELECT 
u.age,
m.genres,
AVG(r.rating) AS avg_rating
FROM ratings r
JOIN users u ON r.userID = u.userID
JOIN movies m ON r.movieID = m.movieID
GROUP BY u.age, m.genres
ORDER BY u.age, avg_rating DESC;


-- 2. TOP 10 higest rated movies-- 

SELECT title,
AVG(r.rating) AS avg_rating,
COUNT(r.rating) AS total_rating
FROM ratings r
JOIN movies m ON r.movieID = m.movieID
GROUP BY r.movieID
HAVING total_rating > 50
ORDER BY avg_rating DESC
LIMIT 10;


-- 3. Most active users (who rated the most movies)-- 

SELECT userID,
COUNT(*) AS total_ratings
FROM ratings
GROUP BY userID
ORDER BY total_ratings DESC
LIMIT 10;

-- 4.TOP genres by age/gender-- 

SELECT u.gender,
u.age,m.genres,
AVG(r.rating) AS avg_rating
FROM ratings r
JOIN users u ON r.userID = u.userID
JOIN movies m ON r.movieID = m.movieID
GROUP BY u.gender, u.age, m.genres
ORDER BY avg_rating DESC;


-- 5.Count users rating more than 500 movies -- 

SELECT userID,
COUNT(*) AS rating_count
FROM ratings
GROUP BY userID
HAVING rating_count > 500;


-- 6.Average rating per movie -- 

SELECT m.title,
AVG(r.rating) AS avg_rating
FROM ratings r 
JOIN movies m ON r.movieID = m.movieID
GROUP BY m.movieID
ORDER BY avg_rating DESC;


-- 7.Most common genre combinstions -- 

SELECT genres,
COUNT(*) AS count_movies
FROM movies
GROUP BY genres
ORDER BY count_movies DESC;


-- 8.Movies rated > 4.5 in the last year -- 

SELECT m.title, r.rating,
FROM_UNIXTIME(r.timestamp) AS rated_on
FROM ratings r
JOIN movies m ON r.movieId = m.movieID
WHERE r.rating > 4.5
AND FROM_UNIXTIME(r.timestamp) > (
SELECT DATE_SUB(MAX(FROM_UNIXTIME(timestamp)), INTERVAL 1 YEAR)
FROM ratings
)
ORDER BY r.rating DESC;