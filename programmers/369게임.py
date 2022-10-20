# 나의 풀이
def solution(order):
  count = 0
  list_order = list(map(int, str(order)))
  for i in list_order:
    if i == 3 or i == 6 or i == 9:
      count += 1
  return count

# 다른 사람 풀이
def solution(order):
  answer = 0
  for i in str(order):
    if int(i) != 0 and int(i) % 3 == 0:
      answer += 1
  return answer
