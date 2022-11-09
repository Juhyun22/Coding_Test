# 2차원 배욜 사용하기 좋았던 문제!
# 문제에서 원하는거 잘 보기!!
T = int(input())
array = []
temp = []

for i in range(T):
    a, b = map(int, input().split(' '))
    temp.append(a)
    temp.append(b)
    temp.append(a + b)
    array[i].append(temp)
    temp = []
    
for i in range(T):
    print('Case #{0}: {1} + {2} = {3}'.format((i + 1), array[i][0], array[i][1], array[i][2]))
    
# 다른 사람 풀이
T = int(input())

for i in range(1, T + 1):
  A, B = map(int, input().split(' '))
  print('Case #' + str(i) + ': ' , A, '+', B, '=', A + B)
