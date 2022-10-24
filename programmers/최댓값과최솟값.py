# 나의 풀이
def solution(s):
  ls = list(map(int, s.split(' ')))
  ls.sort()
  return str(ls[0]) + ' ' + str(ls[-1])

# 다른 사람 풀이
def solution(s):
  s = list(map(int, s.split(' ')))
  retrun str(min(s)) + ' ' + str(max(s))
