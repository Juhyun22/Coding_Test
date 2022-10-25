# 친구스 풀이
from collections import defaultdict

def solution(s):
  answer = ''
  temp =[]
  dict = defaultdict(int)
  for i in s:
    dict[i] += 1
  for k, v in dict.items():
    if v == 1:
      temp.append(k)
  temp.sort()
  answer = ''.join(temp)
  return answer

# 다른 사람 풀이
def solution(s):
  answer = ''.join(sorted([ch for ch in s if s.count(ch) == 1]))
  return answer
