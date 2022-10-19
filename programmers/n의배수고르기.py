# 나의 풀이
def solution(n, numlist):
  answer = []
  for i in numlist:
    if i % n == 0:
      answer.append(i)
  return answer

# 다른 사람 풀이
def solution(n, numlist):
  answer = [i for i in numlist if n % i == 0]
  return answer
