# 나의 풀이
def solution(n):
  answer = []
  for i in str(n):
    i = int(i)
    answer.append(i)
  answer.reverse()
  return answer

# 다른 사람 풀이
def solution(n):
  return list(map(int, reversed(str(n))))
