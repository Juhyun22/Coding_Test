# 나의 풀이
def solution(age):
  answer = ''
  alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
  for i in str(age):
    answer += alpa[int(i)]
  return answer
