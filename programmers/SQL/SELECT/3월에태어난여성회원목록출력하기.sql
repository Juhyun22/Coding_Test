SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d')
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3
and GENDER = 'W' 
and not TLNO is null
order by MEMBER_ID;

# null인지 아닌지 -> is null / not 뭐뭐 is null
# date 출력 이쁘게 -> date_format
# date 달만 뽑아내기 -> month(date)
