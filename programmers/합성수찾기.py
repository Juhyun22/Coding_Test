# 나의 풀이
# 합성수 = 소수를 제외한 수라는 것을 알아서 인터넷에서 소수 찾는 법을 검색하여 모든 수에서 소수를 뺌
# 인터넷 코드를 활용해서 문제 풀이
def solution(n):
  arr = [True] * (n + 1)
  arr[0] = [False]
  arr[1] = [False]
  for i in range(2, n + 1):
    if arr[i] == True:
      j = 2
      while (i * j) <= n:
        arr[i * j] = False
        j += 1
  return (arr.count(False) -2) # 처음에 0에대해서 넣은 값 빼기

# 다른 사람 풀이
def solution(n):
  output = 0
  for i in range(4, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
      if i % j == 0:
        output += 1
        break
  return output
