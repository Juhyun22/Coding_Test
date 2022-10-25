# 나의 풀이
def solution(left, right):
  count = 0
  summ = 0
  for i in range(left, right + 1):
    for j in range(1, i + 1):
      if i % j == 0:
        count += 1
    if count % 2 == 0:
      summ += i
      count = 0
    else:
      summ -= i
      count = 0
  return summ

# 다른 사람 풀이
# 제곱수는 약수의 개수가 홀수,,
def solution(left, right):
  answer = 0
  for i in range(left, right + 1):
    if int(i) ** 0.5 == i ** 0.5:
      answer -= i
    else:
      answer += i
  return answer
