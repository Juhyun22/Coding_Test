# 나의 풀이
def solution(hp):
  count = hp // 5
  temp = hp % 5
  
  count = count + temp // 3
  temp = temp % 3
  
  count = count + temp
  return count

# 다른 사람 풀이
def solution(hp):
  return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
