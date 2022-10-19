# 나의 풀이
def solution(my_string):
  sum = 0
  for i in my_string:
    if i.isdigit():
      sum += int(i)
  return sum

# 다른 사람 풀이
def solution(my_string):
  return sum(int(i) for i in my_string if i.isdigit())
