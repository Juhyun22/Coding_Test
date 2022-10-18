# 나의 풀이
def solution(dot):
    x, y = dot[0], dot[1]

    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
      
# 다른 사람 풀이 1
def solution(dot):
  if dot[0] > 0:
    if dot[1] > 0:
      reutrn 1
    return 4
  else:
    if dot[1] > 0:
      return 2
    return 3
  
# 다른 사람 풀이 2
def solution(dot):
  x, y = dot
  if x * y > 0:
    return 1 if x > 0 else 3
  else:
    return 4 if x > 0 else 2
