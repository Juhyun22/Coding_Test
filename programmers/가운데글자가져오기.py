# 나의 풀이
def solution(s):
  list_s = list(s)
  half_len = len(s) // 2
  if len(s) % 2 != 0:
    return ''.join(list_s[half_len])
  else:
    return ''.join(list_s[half_len - 1] + list_s[half_len])
  
  # 다른 사람 풀이
  def solution(s):
    return str[(len(s) - 1) // 2 : len(s) // 2 + 1]
