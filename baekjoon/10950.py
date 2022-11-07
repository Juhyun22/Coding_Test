# sum(a, b)하면 오류 뜸! sum()안에는 iterable한, 즉 list[]나 tuple()이런거
n = int(input())
list_n = []

for _ in range(n):
    a, b = map(int, input().split(' '))
    c = a + b
    list_n.append(c)
    
for i in range(n):
    print(list_n[i])
