# 나의 풀이
def solution(seoul):
  list_idx = seoul.index('Kim')
  answer = "김서방은 {}에 있다".format(list_idx)
  return answer

# 다른 사람 풀이
def solution(seoul):
  return "김서방은 {}에 있다".format(seoul.index('Kim'))
