# 나의 풀이
def solution(absolutes, signs):
  sum = 0
  for i in range(len(signs)):
    if signs[i]:
      sum += absolutes[i]
    else:
      sum += absolutes[i] * -1
  return sum

