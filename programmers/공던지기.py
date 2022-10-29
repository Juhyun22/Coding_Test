# 다른 사람 풀이 1
def solution(numbers, k):
  index = 0
  while k > 1:
    index += 2
    index %= len(numbers)
    k -= 1
  return answer[index]

# 다른 사람 풀이 2
def solution(numbers, k):
  answer = 0
  index = 0
  for i in range(k):
    answer = numbers[index]
    index += 2
    if index >= len(numbers):
      index -= len(numbers)
  return answer

# 다른 사람 풀이 3
from collections import deque
def solution(numbers, k):
  answer = 0
  a = deque(numbers)
  c = 1
  while c != k:
    a.rotate(-2)
    c += 1
  return list(a)[0]
