# 나의 풀이
def solution(a, b):
  answer = 0
  num1, num2 = min(a, b), max(a, b)
  for i in range(num1, num2 + 1):
    answer += i
  return answer

# 다른 사람 풀이
def solution(a, b):
  if a > b:
    a, b = b, a
  return sum(range(a, b + 1))
