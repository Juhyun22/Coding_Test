# 나의 풀이
def solution(n):
  for i in range(1, n):
    if n % i == 1:
      return i
    
# 다른 사람 풀이
def solution(n):
  return [i for i in range(1, n + 1) if n % i == 1][0]
