# packcge

# import travel.thailand # 마지막은 모듈이나 패키지만 가능 (class 안됨)
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# # 밑에는 가능
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()
