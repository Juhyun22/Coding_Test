# one line for

# 예제 1
# 출석번호가 1 2 3 4 앞에 10을 붙이기로 함 .. 101, 102, ...
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 예제 2
# 학생들 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 예제 3
# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
