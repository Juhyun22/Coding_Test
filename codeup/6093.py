# 거꾸로 출력하기!
# range(n, -1, -1) = range(첫 수, 마지막 수, 증감 거꾸로)
n = int(input())
k = input().split()

for i in range(n - 1, -1, -1):
    print(k[i], end=' ')
