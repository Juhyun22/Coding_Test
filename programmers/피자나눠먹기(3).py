# 간단하고 쉽게! 생각하자!!
def solution(slice, n):
  if n % slice == 0:
    return n // slice
  else:
    return n // slice + 1
