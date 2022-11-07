X = int(input())
N = int(input())
sum_A = 0

for _ in range(N):
    a, b = map(int, input().split(' '))
    sum_A += a * b
 
if X == sum_A:
    print('Yes')
else:
    print('No')
