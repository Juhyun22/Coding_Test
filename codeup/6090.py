# a가 an으로 계속 갱신되어야 함!
# ex) a1 = -1, a2 = 3, ... 이렇게!
# range시에 범위 잘 보기!
a, m, d, n = map(int, input().split())

for i in range(1, n):
    a = a * m + d
    
print(a)
