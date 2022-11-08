# .format()을 이용하기 위해서는 {}.format()형태로 이용
n = int(input())
list_s = []

for _ in range(n):
    a, b = map(int, input().split(' '))
    c = a + b
    list_s.append(c)
    
for x in range(n):
    print('Case #{0}: {1}'.format(x + 1, list_s[x]))
