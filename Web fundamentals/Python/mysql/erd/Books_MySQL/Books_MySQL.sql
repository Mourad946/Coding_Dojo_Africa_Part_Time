-- Step 1: Drop foreign key constraints
ALTER TABLE favorites DROP FOREIGN KEY fk_users_has_books_users1;
ALTER TABLE favorites DROP FOREIGN KEY fk_users_has_books_books1;

-- Step 2: Modify the 'id' columns to AUTO_INCREMENT
ALTER TABLE users MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE books MODIFY COLUMN id INT AUTO_INCREMENT;

-- Step 3: Re-add foreign key constraints
ALTER TABLE favorites ADD CONSTRAINT fk_users_has_books_users1 FOREIGN KEY (user_id) REFERENCES users(id);
ALTER TABLE favorites ADD CONSTRAINT fk_users_has_books_books1 FOREIGN KEY (book_id) REFERENCES books(id);

-- Step 4: Create 5 different users
INSERT IGNORE INTO users (name) VALUES 
('Jane Amsden'), 
('Emily Dixon'), 
('Theodore Dostoevsky'), 
('William Shapiro'), 
('Lao Xiu');

-- Step 5: Create 5 books
INSERT IGNORE INTO books (title, num_of_pages) VALUES 
('C Sharp', 100), 
('Java', 110), 
('Python', 75), 
('PHP', 50), 
('Ruby', 80);

-- Step 6: Change the name of the C Sharp book to C#
UPDATE books SET title = 'C#' WHERE id = 1;

-- Step 7: Change the first name of the 4th user to Bill
UPDATE users SET name = 'Bill Shapiro' WHERE id = 4;

-- Step 8: Have the first user favorite the first 2 books (Avoiding duplicates)
INSERT INTO favorites (user_id, book_id)
SELECT 1, id FROM books WHERE id IN (1, 2) AND NOT EXISTS (
    SELECT 1 FROM favorites WHERE user_id = 1 AND book_id IN (1, 2)
);

-- Step 9: Have the second user favorite the first 3 books (Avoiding duplicates)
INSERT INTO favorites (user_id, book_id)
SELECT 2, id FROM books WHERE id IN (1, 2, 3) AND NOT EXISTS (
    SELECT 1 FROM favorites WHERE user_id = 2 AND book_id IN (1, 2, 3)
);

-- Step 10: Have the fourth user favorite all the books (Avoiding duplicates)
INSERT INTO favorites (user_id, book_id)
SELECT 4, id FROM books WHERE NOT EXISTS (
    SELECT 1 FROM favorites WHERE user_id = 4 AND favorites.book_id = books.id
);

-- Step 11: Retrieve all the users who favorited the 3rd book
SELECT u.name FROM users u INNER JOIN favorites f ON u.id = f.user_id WHERE f.book_id = 3;

-- Step 12: Remove the first user of the 3rd book's favorites
DELETE FROM favorites WHERE user_id = 1 AND book_id = 3;

-- Step 13: Have the 5th user favorite the 2nd book (Avoiding duplicates)
INSERT INTO favorites (user_id, book_id)
SELECT 5, id FROM books WHERE id = 2 AND NOT EXISTS (
    SELECT 1 FROM favorites WHERE user_id = 5 AND book_id = 2
);

-- Step 14: Find all the books that the 3rd user favorited
SELECT b.title FROM books b INNER JOIN favorites f ON b.id = f.book_id WHERE f.user_id = 3;

-- Step 15: Find all the users that favorited the 5th book
SELECT u.name FROM users u INNER JOIN favorites f ON u.id = f.user_id WHERE f.book_id = 5;





