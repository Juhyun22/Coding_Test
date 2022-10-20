# 나의 풀이
def solution(numbers, direction):
  answer = []
  if direction == "right":
    temp = numbers[-1]
    answer.append(temp)
    for i in range(len(numbers) - 1):
      answer.append(numbers[i])
  else:
    temp = numbers[0]
    for i in range(1, len(numbers)):
      answer.append(numbers[i])
    answer.append(temp)
  return answer

# 다른 사람 풀이
def solution(numbers, direction):
  if direction == "right":
    answer = [numbers[-1]] + numbers[:len(numbers) - 1]
  else:
    answer = numbers[1:] + [numbers[0]]
  return answer
