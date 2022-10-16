# 내 풀이
def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    else:
        return 1
      
# 다른 사람 풀이
def solution(angle):
    if angle <= 90:
        return 1 if angle < 90 else 2
    else:
        return 3 if angle < 180 else 4
