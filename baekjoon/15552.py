# 많은 것을 빨리 입력하기 위해서는
# import sys / sys.stdin.readline().split(), sys.stdin.readline.rstrip()
# or pypy 이용!!

import sys

n = int(sys.stdin.readline())
list_sum = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c = a + b
    list_sum.append(c)
    
for i in range(n):
    print(list_sum[i])
