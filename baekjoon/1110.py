num = int(input())
count = 0
temp = num

while True:
    temp_ten = temp // 10
    temp_one = temp % 10
    temp = (temp_ten + temp_one) % 10
    new_num = (temp_one * 10) + temp
    
    count += 1
    if num == new_num:
        break
    temp = new_num
    
print(count)
