# 나의 풀이
# 제대로 제거 되는지 확인
def solution(my_string):
  answer = my_string
  dell = ['a', 'e', 'i', 'o', 'u']
  for i in range(5):
    answer = answer.replace(dell[i], '')
  return answer
