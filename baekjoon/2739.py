# str + int로 출력 불가!! 꼭 str로 바꿔줄것!!!!
n = int(input())

for i in range(1, 10):
    print(str(n) + ' * ' + str(i) + ' = ' + str(n * i))
