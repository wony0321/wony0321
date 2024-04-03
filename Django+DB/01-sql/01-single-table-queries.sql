-- 01. Querying data
-- SELECT 필드명 FROM 테이블명;

SELECT 
  LastName
FROM
  employees;

SELECT 
  LastName, FirstName
FROM
  employees;

SELECT 
  *
FROM
  employees;

SELECT 
  FirstName AS '이름'
FROM
  employees;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName ASC;

SELECT 
  Country, City
FROM
  customers
ORDER BY 
  Country DESC,
  City ASC;

SELECT 
  Name,
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;

-- NULL 정렬 예시
SELECT 
  ReportsTo
FROM
  employees
WHERE ReportsTo IS NOT NULL
ORDER BY
  ReportsTo DESC;

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

-- 03. Filtering data
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL
  -- 논리연산자 AND 사용해야 함!
  OR Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- Bytes >= 100000 AND Bytes <= 500000
  Bytes BETWEEN 100000 AND 500000
ORDER BY Bytes;

SELECT
  LastName, FirstName, Country
FROM
  customers
WHERE
  -- 값이 특정 목록 안에 있는지 확인
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  -- 0개 이상의 문자열과 일치하는지 확인
  LastName LIKE '%son';

SELECT
  LastName, FirstName
FROM
  customers
WHERE
  -- 단일 문자와 일치하는지 확인
  FirstName LIKE '___a';



SELECT
  TrackId, Name, Bytes
FROM
  tracks
-- 조회하는 레코드 수를 제한
ORDER BY 
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;


-- 04. Grouping data
-- 집계함수와 같이 쓰임
SELECT
  Country, COUNT(*)
FROM
  customers
GROUP BY
  -- 이것만 하면 distinct랑 같아짐
  -- but 단일한 요약본 만드는게 다름
  Country;

SELECT
  Composer, 
  AVG(Bytes) AS avgOfBytes,
  AVG(Milliseconds/60000) AS avgOfMinute
FROM
  tracks
GROUP BY 
  Composer
-- group에서는 where 조건 쓸 수 없음
HAVING
  avgOfMinute < 10;
-- ORDER BY
--   avgOfBytes DESC;