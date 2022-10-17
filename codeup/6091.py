# 최소공배수 문제! 세 수 모두 나눠질 시에 답이 나옴! 
# ex) 3, 7, 9의 최소공배수는 63!
a, b, c = map(int, input().split())
d = 1

while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1 
    
print(d)
