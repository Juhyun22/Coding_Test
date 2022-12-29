n = int(input())
score = list(map(int, input().split()))
    
max_s = max(score)
summ = 0

for i in score:
    summ += i / max_s * 100
    
print(summ/n)
