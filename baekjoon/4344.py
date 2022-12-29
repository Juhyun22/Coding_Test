n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    
    num = arr[0]
    arr.remove(num)
    summ = sum(arr)
    avg = summ / num
    count = 0
    
    for i in arr:
        if i > avg:
            count += 1
            
    per = (count / num) * 100  
    print('%.3f' %per + '%')
