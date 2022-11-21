n = int(input())
n_list = list(map(int, input().split()))
find_n = int(input())    
count = 0

for i in n_list:
    if i == find_n:
        count += 1
 
print(count)
