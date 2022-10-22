# 나의 풀이
def solution(n):
  for i in range(1, n + 1):
    if i * i == n:
      return (i + 1) * (i + 1)
   return -1

# 다른 사람 풀이
def solution(n):
  sqrt = n ** 0.5
  if sqrt % 1 == 0: # 정수가 아닐 때,
    return (sqrt + 1) ** 2
  return -1
