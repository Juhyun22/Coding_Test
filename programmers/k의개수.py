# 나의 풀이
def solution(i, j, k):
  count = 0
  for num in range(i, j + 1):
    if str(k) in str(num):
      count += str(num).count(str(k))
  return count

# 다른 사람 풀이
def solution(i, j, k):
  answer = sum([str(i).count(str(k)) for i in range(i, j + 1)])
  return answer
