# 나의 풀이
def solution(my_string):
  result = []
  my_list = list(my_string)
  for value in my_list:
    if value not in result:
      result.append(value)
  return ''.join(result)

# 다른 사람 풀이
def solution(my_string):
  answer = []
  for i in my_string:
    if answer.count(i) == 0:
      answer.append(i)
  return ''.join(answer)
