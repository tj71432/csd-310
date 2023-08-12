/*
Taylor Jacobs
CYBR410 - Database Security
Prof. Peter Haas
7/23/2023
*/

SELECT whatabook;
-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('Frankenstein', 'Mary Shelley', 'Some book about Frankenstein');

INSERT INTO book(book_name, author, details)
    VALUES('Ace Dune', 'Frank Herbert', 'Its chill');

INSERT INTO book(book_name, author, details)
    VALUES('Simon & Schuster The Martian Chronicles', 'Ray Bradbury', "not sure");

INSERT INTO book(book_name, author)
    VALUES('Orbit The Fifth Season', 'N.K. Jemisin');

INSERT INTO book(book_name, author)
    VALUES('Ace The Left Hand of Darkness', 'Ursula K. Le Guin');

INSERT INTO book(book_name, author)
    VALUES('Beacon Press Kindred', 'Octavia Butler');

INSERT INTO book(book_name, author)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald');

INSERT INTO book(book_name, author)
    VALUES('Vintage Never Let Me Go', 'Kazuo Ishiguro');

INSERT INTO book(book_name, author)
    VALUES('The Catcher and the Rye', 'J.D. Salinger');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Dwayne', 'Johnson');

INSERT INTO user(first_name, last_name)
    VALUES('John', 'Doe');

INSERT INTO user(first_name, last_name)
    VALUES('Jane', 'Doe');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Dwayne'), 
        (SELECT book_id FROM book WHERE book_name = 'Ace Dune')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'John'),
        (SELECT book_id FROM book WHERE book_name = 'Vintage Never Let Me Go')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jane'),
        (SELECT book_id FROM book WHERE book_name = 'Orbit The Fifth Season')
    );
