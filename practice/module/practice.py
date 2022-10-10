# module
# 필요한 것만 모인 것

# 예제 1
import theather_module
theather_module.price(3) # 3명이서 영화보러 갔을 때 가격 
theather_module.price_morning(4) # 4명이서 조조할인 보러 갔을 때
theather_module.price_soldier(5) # 5명의 군인이 영화보러 갔을 때

# 예제 2
# 모듈 이름이 길 때에 별명으로 바꿀 수 있음
import theather_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# 예제 3
from theather_module import *
price(3)
price_morning(4)
price_soldier(5)

# 예제 4
# 필요한 함수만 import
from theather_module import price, price_morning, price_soldier
price(3)
price_morning(4)
# error .. price_soldier(5)

# 예제 5
from theather_module import price_soldier as price
price(5) # price_soldier의 가격
