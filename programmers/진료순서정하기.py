# 나의 풀이
def solution(emergency):
  answer = [0] * len(emergency)
  count = 1
  for _ in emergency:
    temp = max(emergency)
    idx = emergency.index(temp)
    answer[idx] = count
    emergency[idx] = -1
    count += 1
  return answer

# 다른 사람 풀이
def solution(emergency):
  return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
