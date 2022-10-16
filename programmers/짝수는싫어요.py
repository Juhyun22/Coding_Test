# 내 풀이
def solution(n):
    answer = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            answer.append(i)
        else:
            continue

    return answer
  
  # 다른 사람 풀이
  def solution(n):
    return [i for i in range(1, n+1, 2)]
