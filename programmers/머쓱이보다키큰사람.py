# 나의 풀이
def solution(array, height):
    count = 0

    for i in range(len(array)):
        if array[i] > height:
            count += 1

    return count

# 다른 사람 풀이
def solution(array, height):
    return len([i for i in array if i > height])
