# 나의 풀이
def solution(n):
  for i in range(1, 1001):
    if i ** 2 == 0:
      return 1
  return 2

# 다른 사람 풀이 1
def solution(n):
  return 1 if (n ** 0.5).is_integer() else 2

# 다른 사람 풀이 2
def solution(n):
  for i in range(1, n):
    if n == i * i:
      return 1
  return 2
