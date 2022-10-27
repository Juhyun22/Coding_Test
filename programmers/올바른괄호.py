# 다른 사람 풀이
# 문제 풀이 잘 해봐야 할듯
def solution(s):
  openn = '('
  close = ')'
  count = 0
  for char in s:
    if char == openn:
      count += 1
    if char == close:
      count -= 1
    if count < 0:
      return False
  return count == 0
