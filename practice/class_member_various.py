# 멤버 변수

# 예제 1
# class 내에서 정의된 변수
# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# 마인트 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# class 외부의 확장이 가능함
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
