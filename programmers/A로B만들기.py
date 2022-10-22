# 나의 풀이
# ㅋㅋㅋㅋ... 진짜...!!!
def solution(before, after):
  list_before = list(before)
  list_after = list(after)
  for i in range(len(list_before)):
    if list_before[i] in list_after:
      list_after.remove(list_before[i])
  if len(list_after):
    return 0
  else:
    return 1
  
# 다른 사람 풀이
def solution(before, after):
  before = sorted(before)
  after = sorted(after)
  if before == after:
    return 1
  else:
    return 0
