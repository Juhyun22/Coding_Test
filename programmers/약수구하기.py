# 나의 풀이
def solution(n):
  answer = []
  for i in range(1, n + 1):
    if n % i == 0:
      answer.append(i)
  return answer

# 다른 사람 풀이
def solution(n):
  answer = [i for i in range(1, n + 1) if (n % i) == 0]
  return answer
