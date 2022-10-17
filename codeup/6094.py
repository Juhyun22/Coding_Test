# 입력을 받으면 int로 변환해주지 않는 이상, str이다!
n = int(input())
k = input().split()

for i in range(n):
    k[i] = int(k[i])
    
print(min(k))

# 받을 때 int로 받기
n = int(input())
k = map(int, input().split())

print(min(k))
