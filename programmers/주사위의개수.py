# 나의 풀이
def solution(box, n):
  answer = 1
  for i in box:
    answer *= i // n
  return answer

# 다른 사람 풀이
def solution(box, n):
  w, h, d = box[0] // n, box[1] // n, box[2] // n
  return w * h * d
