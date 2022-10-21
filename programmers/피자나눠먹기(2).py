# 나의 풀이
def solution(n):
  answer = 0
  i = 1
  while True:
    if (6 * i) % n == 0:
      break
    i += 1
  answer = i
  return answer

# 다른 사람 풀이
def solution(n):
  answer = 1
  while 6 * answer % n:
    answer += 1
  return answer
