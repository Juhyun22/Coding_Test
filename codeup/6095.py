d = []                      # 바둑판 생성
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)
        
n = int(input())            # 바둑판에서 놓을 수 받기
for i in range(n):
    x, y = input().split()  # 위치 받기 
    d[int(x)][int(y)] = 1   # 위치 저장
    
for i in range(1, 20):      # 바둑판에서는 (0,0)이 아니라 (1,1)부터 시작! 그리고 19 * 19 판의 바둑판임!
    for j in range(1, 20):
        print(d[i][j], end=' ')
    print()
