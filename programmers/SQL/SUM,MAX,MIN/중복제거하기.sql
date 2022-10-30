# 중복된 개수 제거는 count(distinct(column))
SELECT COUNT(DISTINCT(name))
FROM ANIMAL_INS
WHERE NAME is not null
