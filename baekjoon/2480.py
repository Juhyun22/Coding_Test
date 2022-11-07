# 정렬 시에는 a.sort() / a.reverse()의 형태로 쓴다!!
a = list(map(int, input().split()))
prize = 0

a.sort()

if a[0] == a[1] and a[0] == a[2]:
    prize = 10000 + a[0] * 1000
elif a[0] == a[1] or a[1] == a[2]:
    if a[0] == a[1]:
        prize = 1000 + a[0] * 100
    else:
        prize = 1000 + a[1] * 100
else:
    prize = a[2] * 100

print(prize)
