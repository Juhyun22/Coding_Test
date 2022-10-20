# 나의 풀이
def solution(my_string, num1, num2):
  list_my = list(my_string)
  temp = []
  temp = list_my[num1]
  list_my[num1] = list_my[num2]
  list_my[num2] = temp
  return ''.join(list_my)

# 다른 사람 풀이
def solution(my_string, num1, num2):
  s = list(my_string)
  s[num1], s[num2] = s[num2], s[num1]
  return ''.join(s)
