# 나의 풀이
def solution(my_string):
  answer = ''
  for i in my_string:
    if i.isupper():
      i = i.lower()
      answer += i
    else:
      i = i.upper()
      answer += i
   return answer

# 다른 사람 풀이
def solution(my_string):
  return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
