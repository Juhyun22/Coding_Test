# 나의 풀이
def solution(x, n):
  answer = []
  for i in range(1, n + 1):
    answer.append(i * x)
  return answer

# 다른 사람 풀이
def solution(x, n):
  return [i * x for i in range(1, n + 1)]
