# 내장 함수
# builtins function

# 예제 1
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요")
print("{0}은 아주 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random # 외장 함수
print(dir())
import pickle
print(dir())

print(dir(random)) # random 모듈 내에서 쓸 수 있는 것들이 나옴

# 예제 2
lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))

# list of python builtins
