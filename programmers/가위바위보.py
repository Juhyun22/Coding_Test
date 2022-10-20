# 나의 풀이
def solution(rsp):
  answer = ''
  for i in rsp:
    if int(i) == 2:
      answer += '0'
    elif int(i) == 0:
      answer += '5'
    else:
      answer += '2'
  return answer
  
# 다른 사람 풀이
def solution(rsp):
  d = {'0' : 5, '2' : '0', '5' : '2'}
  return ''.join(d[i] for i in rsp)
