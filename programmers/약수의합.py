# 나의 풀이
def solution(n):
  sum = 0
  for i in range(1, n + 1):
    if n % i == 0:
      sum += n / i
  return sum

# 다른 사람 풀이
def solution(n):
  return sum([i for i in range(1, n + 1) if n % i == 0])
