# 어떻게 입출력 되는지 확인 잘 하기!!
n, x = map(int, input().split())
list_n = list(map(int, input().split()))

for i in list_n:
    if i < x:
        print(i, end=' ')
