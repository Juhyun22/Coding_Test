# 나의 풀이
def solution(n):
  num = []
  for i in range(1, n + 1):
    if n % i == 0:
      num.append(i)
  return len(num)

# 다른 사람 풀이
def solution(n):
  return len([i for i in range(1, n + 1) if n % i == 0])
