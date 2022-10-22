# 나의 풀이
def solution(s):
  cnt_p = 0
  cnt_y = 0
  for i in s:
    if i == 'p' or i == 'P':
      cnt_p += 1
    elif i == 'y' ir i == 'Y':
      cnt_y += 1
  if cnt_p == cnt_y:
    return True
  return False

# 다른 사람 풀이
def solution(s):
  return s.lower().count('p') == s.lower().count('y')
