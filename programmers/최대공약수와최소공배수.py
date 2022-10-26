# 나의 풀이
import math

def solution(n, m):
answer = []
answer.append(math.gcd(n, m))
for i in range(max(n, m), (n * m) + 1):

