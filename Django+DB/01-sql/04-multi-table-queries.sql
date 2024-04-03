-- 공통
SELECT * FROM article;
SELECT * FROM users;
DROP TABLE article;
DROP TABLE users;
PRAGMA table_info('article');


-- 실습용 데이터
-- CREATE TABLE users (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE article (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   title VARCHAR(50) NOT NULL,
--   content VARCHAR(100) NOT NULL,
--   userId INTEGER NOT NULL,
--   FOREIGN KEY (userId) 
--     REFERENCES users(id)
-- );

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  article (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

-- INNER JOIN

-- user 데이터가 앞쪽에 위치
SELECT * FROM users
INNER JOIN article
  ON users.id = article.userID;

-- article 데이터가 앞쪽에 위치
SELECT * FROM article
INNER JOIN users
  ON article.userID = users.id;

SELECT * FROM article
OUTER JOIN users
  ON article.userID = users.id;

SELECT article.title, users.name FROM article
INNER JOIN users
  ON users.id = article.userID
  WHERE users.id = 1;

-- LEFT JOIN
SELECT *
FROM article
LEFT JOIN users
  ON article.userId = users.id;

SELECT *
FROM article
RIGHT JOIN users
  ON article.userId = users.id;

  -- 게시글을 작성한 적이 없는 사람
SELECT *
FROM users
LEFT JOIN article
  ON users.id = article.userId
WHERE article.userId IS NULL;