# 문제 끝까지 잘 읽기!
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IF(TLNO is null, 'NONE', TLNO) AS TLNO
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12
ORDER BY AGE DESC, PT_NAME
