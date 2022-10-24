SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = '3' and not TLNO is null

# null인지 아닌지 -> is null / not 뭐뭐 is null
