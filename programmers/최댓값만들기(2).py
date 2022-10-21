# 나의 풀이
def solution(numbers):
  answer = 0
  numbers.sort()
  multi1 = numbers[0] * numbers[1]
  multi2 = numbers[-1] * numbers[-2]
  if multi1 > multi2:
    answer = multi1
  else:
    answer = multi2
  return answer

# 다른 사람 풀이
def solution(numbers):
  numbers = sorted(numbers)
  return max(numbers[0] * numbser[1], numbers[-1] * numbers[-2])
