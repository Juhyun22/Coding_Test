# 나의 풀이
def solution(strlist):
  answer = []
  
  for i in range(len(strlist)):
    answer.append(len(strlist[i]))
    
  return answer

# 다른 사람 풀이 1
def solution(strlist):
  answer = []
  for i in strlist:
    answer.append(len(i))
  return answer

# 다른 사람 풀이 2
def solution(strlist):
  return [len(str) for str in strlist]
