# 나의 풀이
def solution(my_str, n):
  list_str = list(my_str)
  store = []
  if len(my_str) % n == 0:
    nx = len(my_str) // n
  else:
    nx = len(my_str) // n + 1
  for i in range(nx):
    store_str = ''.join(list_mystr[i * n : (i + 1) * n])
    store.append(store_str)
  return store

# 다른 사람 풀이
def solution(my_str, n):
  return [my_str[i : i + n] for i in range(0, len(my_str), n)]
