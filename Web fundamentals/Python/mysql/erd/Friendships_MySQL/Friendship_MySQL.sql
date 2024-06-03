CREATE TABLE users (
    id INT PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30)
);

CREATE TABLE friendships (
    id INT PRIMARY KEY,
    user_id INT,
    friend_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
);

INSERT INTO users (id, first_name, last_name)
VALUES (1, 'John', 'Doe'),
       (2, 'Jane', 'Doe'),
       (3, 'Jim', 'Smith'),
       (4, 'Joe', 'Black'),
       (5, 'Alice', 'White'),
       (6, 'Bob', 'Brown');

INSERT INTO friendships (id, user_id, friend_id)
VALUES (1, 1, 2),
       (2, 1, 4),
       (3, 1, 6),
       (4, 2, 1),
       (5, 2, 3),
       (6, 2, 5),
       (7, 3, 2),
       (8, 3, 5),
       (9, 4, 3),
       (10, 5, 1),
       (11, 5, 6),
       (12, 6, 2),
       (13, 6, 3);

SELECT user2.first_name, user2.last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 1;