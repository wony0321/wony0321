-- 공통
SELECT * FROM articles;
DROP TABLE articles;

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

PRAGMA table_info('articles');


-- 1. Insert data into table
INSERT INTO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-02');

INSERT INTO articles
-- 필드 생략도 가능하지만
-- 모든 필드의 값 넣어주어야 함!
VALUES (2, 'hello', 'world', '2000-01-02');

INSERT INTO articles (title, content, createdAt)
VALUES 
('hello', 'world', '2000-01-03'),
('hello', 'world', '2000-01-04')
;

INSERT INTO articles (title, content, createdAt)
VALUES 
('hello', 'world', DATE()),
('hello', 'world', DATE())
;

-- 2. Update data in table

UPDATE articles
SET title = 'HOME';


UPDATE articles
SET title = 'SSAFY'
WHERE content = 'world';

UPDATE articles
SET title = 'Update Title'
WHERE id = 1;

UPDATE articles
SET Title = 'Update Title',
    content = 'Update Content'
WHERE id = 2;

-- 3. Delete data from table

