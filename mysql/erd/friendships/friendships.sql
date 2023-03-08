INSERT INTO users (first_name,last_name)
VALUES ('Jaden','Yuki'),('Cyrus','Truesdale'),('Chazz','Princeton'),('Alexis','Rhodes'),('Mr.','Crowler'),('Chumley',NULL);

INSERT INTO friendships (user_id,friend_id)
VALUES (1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(3,2),(3,5),(4,3),(5,1),(5,6),(6,2),(6,3);

SELECT * FROM users
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users AS user2 ON user2.id=friendships.friend_id;

SELECT * FROM users
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users AS user2 ON user2.id=friendships.friend_id
WHERE users.id = 1;

SELECT * FROM users
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users AS user2 ON user2.id=friendships.friend_id
WHERE users.id = 3
ORDER BY users.first_name;