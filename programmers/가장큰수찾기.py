# 나의 풀이
def solution(array):
  answer = [0, 0]
  answer[0] = max(array)
  answer[1] = array.index(answer[0])
  return answer

# 다른 사람 풀이
def solution(array):
  return [max(array), array.index(max(array))]
