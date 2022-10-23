# 나의 풀이
def solution(phone_number):
  list_p = list(phone_number)
  for i in range(len(list_p) - 4):
    list_p[i] = '*'
  return ''.join(list_p)

# 다른 사람 풀이
def solution(phone_number):
  return '*' * (len(phone_number) - 4) + phone_number[-4:]
