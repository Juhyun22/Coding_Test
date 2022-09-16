# Quiz6

height = 175
gender = "남자"
agv_kg = 0

def std_weight(height, gender, agv_kg):
    if gender == "남자":
        agv_kg = height * height * 22
        return agv_kg / 100
    else:
        agv_kg = height * height * 21
        return agv_kg / 100
    
agv_kg = std_weight(height, gender, agv_kg)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, agv_kg))

# 풀이
def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
    
