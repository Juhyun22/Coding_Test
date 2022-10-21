# 다른 사람 풀이 1
def solution(num_list, n):
  answer = []
  cnt = 0
  temp = []
  for num in num_list:
    temp.append(num)
    cnt += 1
    if cnt == n:
      answer.append(temp)
      temp = []
      cnt = 0
  return answer

# 다른 사람 풀이 2
def solution(num_list, n):
  answer = []
  for i in range(len(num_list) // n):
    answer.append(num_list[i * n : (i + 1) * n])
  return answer
