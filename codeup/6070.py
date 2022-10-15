# 내 풀이
month = int(input())

if month // 3 == 0:
    print("winter")
elif month // 3 == 1:
    print("spring")
elif month // 3 == 2:
    print("summer")
elif month // 3 == 3:
    print("fall")
else:
    print("winter")
    
# month // 3 == 0을 지우고 else에 넣으면 깔끔함
month = int(input())

if month // 3 == 1:
  print("spring")
elif month // 3 == 2:
  print("summer")
elif month // 3 == 3:
  print("fall")
else:
  print("winter")
