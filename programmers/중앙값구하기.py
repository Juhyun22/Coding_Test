def solution(array):
    answer = 0
    array.sort()
    mid = int(len(array) / 2)
    answer = array[mid]
    return answer 
  
  # 다른 풀이
numbers = [1, 4, 3, 2, 5]
answer = 0

numbers = sorted(numbers)
numbers[len(numbers) // 2]
