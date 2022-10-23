# 나의 풀이
def solution(arr):
  num_idx = min(arr)
  if len(arr) == 1:
    return [-1]
  arr.remove(num_idx)
  return arr

# 다른 사람 풀이
def solutin(arr):
  return [i for i in arr if i > min(arr)] or [-1]
