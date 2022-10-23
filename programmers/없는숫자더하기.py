# 나의 풀이
def solution(numbers):
  sum = 0
  for i in range(10):
    if i not in numbers:
      sum += i
  return sum

# 다른 사람 풀이
def solution(numbers):
  return 45 - sum(numbers)
