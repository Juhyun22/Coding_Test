# 나의 풀이
def solution(n):
  n = str(n)
  list_n = list(n)
  list_n.sort(reverse=True)
  return int(''.join(list_n))
