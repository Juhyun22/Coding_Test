# 나의 풀이
# 문제 꼼꼼히 잘 읽을것!!
def solution(s):
  if (len(s) == 4 or len(s) == 6) and s.digit():
    return True
  return False

# 다른 사람 풀이
# 크으으으.. 
def solution(s):
  return s.digit() and len(s) in (4, 6)
