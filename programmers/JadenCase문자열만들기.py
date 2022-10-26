# 나의 풀이
def solution(s):
  ls = s.split(' ')
  strl = []
  for i in ls:
    stri = i.caplialize()
    strl.append(stri)
  return ' '.join(strl)
