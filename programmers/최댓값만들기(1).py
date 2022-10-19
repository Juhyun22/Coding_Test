# 나의 풀이
# python에는 sort라는 좋은 기능이 있다 .. 아는게 답!!
def solution(numbers):
  max1 = max(numbers)
  numbers.remove(max1)
  max2 = max(numbers)
  return max1 * max2

# 다른 사람 풀이
def solution(numbers):
  numbers.sort()
  return numbers[-2] * numbers[-1]
