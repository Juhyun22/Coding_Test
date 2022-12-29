numbers = []

for i in range(10):
    num = int(input())
    num = num % 42
    
    if num in numbers:
        continue
        
    numbers.append(num)
    
print(len(numbers))
