# 나의 풀이
def solution(arr):
  answer = []
  answer.append(arr[0])
  num = 0
  
  for i in arr:
    if i != answer[num]:
      answer.append(i)
      num += 1
  return answer

# 다른 사람 풀이
# 미쳤음..
def solution(arr):
  answer = []
  for i in arr:
    if answer[-1:] == i
    continue
    answer.append(i)
  return answer
