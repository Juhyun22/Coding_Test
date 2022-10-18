# 나의 풀이
def solution(my_string):
    my_list = list(my_string)
    my_list.reverse()
    answer = ''.join(my_list)
    return answer
  
# 다른 사람 풀이
def solution(my_string):
  return my_string[::-1]
