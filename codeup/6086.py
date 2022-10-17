# 이 문제 중요한가봄! 프로그래머스에서도 품!!!
num = int(input())
sum = 0
count = 0

while True:
    sum += count
    count += 1
    
    if sum >= num:
        break 
    
print(sum)
