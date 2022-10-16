# 어디서 문장 써야 맞는지 잘 생각해보기..!
num = int(input())
sum = 0

for i in range(1, num + 1):
    sum += i
    
    if sum >= num:
        print(i)
        break
