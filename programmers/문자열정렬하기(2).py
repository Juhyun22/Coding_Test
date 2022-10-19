# 나의 풀이
# 배열이 아닌 문자열은 값 변경 시 따로 저장
def solution(my_string):
  s = my_string.lower()
  answer = ''.join(sorted(s))
  return answer

# 다른 사람 풀이
def solution(my_string):
  return ''.join(sorted(my_string.lower()))
