# 나의 풀이
def solution(num, k):
  num_list = list(map(int, str(num)))
  if not k in num_list:
    return -1
  return num_list.index(k) + 1

# 다른 사람 풀이
def solution(num, k):
  answer = (str(num).find(str(k)) + 1)
  if answer == 0:
    return -1
  return answer
