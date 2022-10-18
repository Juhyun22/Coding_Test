# 나의 풀이 
def solution(n):
  answer = 0
  
  while n > 0:
    answer += n % 10
    n = n // 10
    
  return answer

# 다른 사람 풀이
def solution(n):
  N = [int(i) for i in str(n)]
  return sum(N)
