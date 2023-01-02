# 입력받는거 잘 확인
# 변수 잘 확인

t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    word = ''
    
    for j in s:
        word += j * r
   
    print(word)
