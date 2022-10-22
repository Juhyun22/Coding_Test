# 나의 풀이
def solution(x):
  num = 0
  for i in str(x):
    sum += int(i)
  if x % n == 0:
    return True
  return False

# 다른 사람 풀이
def solution(x):
  return x % sum([int(n) for n in str(x)]) == 0
