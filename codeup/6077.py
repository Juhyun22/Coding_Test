# 0은 더해도 의미 없고 시간만 쓰니 range(1, n+1)이 나음!
n = int(input())
s = 0

for i in range(0, n + 1): 더 
    if i % 2 == 0:
        s += i

print(s)
