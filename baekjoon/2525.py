# 두번 해보고 안되면 visual studio code로 적어서 뭐가 문제인지 확인!!
# 생각 잘 하고 풀자ㅠㅜㅠㅠ
h, m = map(int, input().split(' '))
oven_time = int(input())

m = (oven_time % 60) + m
h = (oven_time // 60) + h

if m >= 60:
    m = m - 60
    h += 1
    
if h >= 24:
    h = h - 24
    
print(h, m)
