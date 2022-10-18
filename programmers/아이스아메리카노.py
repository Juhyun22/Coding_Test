# 나의 풀이
def solution(money):
  answer = []
  answer.append(money // 5500)
  answer.append(money % 5500)
  return answer

# 다른 사람 풀이 1
def solution(money):
  answer = [money // 5500, money % 5500]
  return answer

# 다른 사람 풀이 2
def solution(money):
  return divmod(money, 5500)
