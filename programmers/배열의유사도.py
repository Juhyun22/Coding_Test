# 나의 풀이
def solution(s1, s2):
  count = 0
  
  for i in s1:
    if i in s2:
      count += 1
      
  return count

# 다른 사람 풀이
def solution(s1, s2):
  return len(set(s1) & set(s2))
