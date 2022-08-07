# 1부터 20명 중에 치킨 당첨자 1명, 커피 당첨자 3명
# 랜덤으로 돌리기
# 치킨, 커피 중복 당첨 안됨

from random import *
users = range(1, 21) # 1부터 20까지 숫자 생성
# print(type(users))
users = list(users)

# shuffle(users)
# print(users)

winners = sample(users, 4) # 4면 중에 한명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", winners[0]) # print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : ", winners[1:])
print("-- 축하합니다 -- ")

# 1. set으로 중복 제거 -> 복잡
# 2. list로 4명 뽑기 -> 위의 방법 
