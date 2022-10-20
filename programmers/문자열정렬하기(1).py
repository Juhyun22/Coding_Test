# 나의 풀이
def solution(my_string):
  answer = []
  for i in my_string:
    if i.isdigit():
      answer.append(int(i))
  answer.sort()
  return answer

# 다른 사람 풀이
def solution(my_string):
  return sorted([int(c) for c in my_string if c.isdigit()])
