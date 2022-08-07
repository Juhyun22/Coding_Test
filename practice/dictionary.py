# dictionary
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

# 사전에서 자료형 가져오기
print(cabinet.get(3))
# print(cabinet[5]) 5라는 키 없음 -> 오류 즉, 끝
print(cabinet.get(5)) # none으로 출력하고 실행
print(cabinet.get(5, "사용 가능")) # 5 열쇠 출력
print("hi")

# key 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet2["A-3"])
print(cabinet2["B-100"])

# 새 손님
print(cabinet2)
cabinet2["A-3"] = "김종국"
cabinet2["C-20"] = "조세호"
print(cabinet2)

# 간 손님
del cabinet2["A-3"]
print(cabinet2)

# key 들만 출력
print(cabinet2.keys()) # () 넣기

# value 들만 출력
print(cabinet2.values())

# key, value 쌍으로 출력
print(cabinet2.items())

# 전체 삭제
cabinet2.clear()
print(cabinet2)
