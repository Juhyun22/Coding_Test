# 나의 풀이
def solution(n, k):
    answer = n * 12000 + k * 2000
    service = (n // 10) * 2000

    answer = answer - service

    return answer
  
  # 다른 사람 풀이
  def solution(n, k):
    return (n * 12000) + 2000 * (k - n // 10)
