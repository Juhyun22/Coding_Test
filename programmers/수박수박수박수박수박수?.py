# 나의 풀이
def solution(n):
  wm = '수박'
  ans = ''
  for i in range(n):
    if i % 2 == 0:
      ans += wm[0]
    else:
      ans += wm[1]
  return ans

# 다른 사람 풀이 1
def solution(n):
  s = '수박' * n
  return s[:n]

# 다른 사람 풀이 2
def solution(n):
  return '수박' * (n // 2) + '수' * (n % 2)
