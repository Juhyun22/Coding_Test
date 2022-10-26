# 나의 풀이
# 잘 생각 했지만 더 생각해야함!!
def solution(array, n):
  ls = list(array)
  ls.append(n)
  ls.sort()
  if ls[-1] == n:
    return ls[-2]
  n_idx = ls.index(n)
  a = n_idx - 1
  b = n_idx + 1
  if abs(n - ls(a)) > abs(n - ls(b)):
    return ls[b]
  else:
    return ls[a]
  
  # 다른 사람 풀이
  def solution(array, n):
    array.sort()
    temp = []
    for i in array:
      temp.append(abs(n - i))
    return array[temp.index(min(temp))]
