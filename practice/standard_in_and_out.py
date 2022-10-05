# 표준 입출력

# 예제 1 
# end = 문장의 끝 부분을 ?로 바꿔달라.
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

# 예제 2
# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 예제 3
# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=",")
    
# 예제 4
# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    
# 에제 5
# 사용자 값을 받으면 항상 문자열
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")
