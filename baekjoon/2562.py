arr = []

for i in range(9):
    num = int(input())
    arr.append(num)
    
find_num = max(arr)
print(find_num)
print(arr.index(find_num) + 1)
