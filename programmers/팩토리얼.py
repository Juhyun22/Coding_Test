# 나의 풀이
def solution(n):
  fac = 1
  for i in range(1, 10 + 1):
    fac *= i
    if fac == n:
      return i
    elif fac < n:
      return i - 1
    
# 다른 사람 풀이
from math import factorial

def solution(n):
  k = 10
  while n < factorial(k):
    k -= 1
  return k
