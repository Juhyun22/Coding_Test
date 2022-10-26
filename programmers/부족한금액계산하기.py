# 나의 풀이
# 문제 천천히 잘 읽어보구 풀자ㅠㅠ
def solution(price, money, count):
  answer = 0
  temp = money
  for i in range(1, count + 1):
    temp = temp - (price * i)
  if temp > 0:
    return 0
  return abs(temp)
