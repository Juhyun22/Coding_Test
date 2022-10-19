# 나의 풀이
def solution(my_string, n):
  store = []
  answer = ''
  for i in my_string:
    store.append(i)
    
  for i in store:
    for j in range(n):
      answer += i
      
   return answer

# 다른 사람 풀이
def solution(my_string, n):
  return ''.join(i * n for i in my_string)
