# 나의 풀이
def solution(num):
  answer = 0
  if num == 1:
    return 0
  for i in range(500):
    if num % 2 == 0:
      num = num // 2
    else:
      num = (num * 3) + 1
    if num == 1:
      return i + 1
  return -1

# 다른 사람 풀이
def solution(num):
  if num == 1: 
    return 0
  for i in range(500):
    num = num / 2 if num % 2 == 0 else num = num * 3 + 1
    if num == 1:
      return i + 1
  return -1
