# 나의 풀이
def solution(sides):
  sides.sort()
  two_len_sum = sides[0] + sides[1]
  
  if sides[-1] < two_len_sum:
    return 1
  else:
    return 2
  
# 다른 사람 풀이
def solution(sides):
  return 1 if max(sides) < (sum(sides) - max(sides)) else 2
