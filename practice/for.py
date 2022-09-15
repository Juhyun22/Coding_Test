# 반복문 for문
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")

# randrange()
for waiting_no in [0, 1, 2, 3, 4]: # range(5) / range(1, 6)
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
