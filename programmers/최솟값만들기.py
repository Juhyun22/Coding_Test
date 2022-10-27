# 나의 풀이
def solution(A, B):
  answer = 0
  A.sort()
  B.sort(reverse=True)
  for i in range(len(A)):
    answer += A[i] * B[i]
  return answer

# 다른 사람 풀이
def solution(A, B):
  return sum(a * b for a, b in zip(sorted(A), sorted(B, reverse=True)))
