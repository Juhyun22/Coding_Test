# 소수점 자리 출력 -> f"{num: .2f}" or "{:.2f}".format(num)
# 소수점 어디까지 출력되는지 잘 확인!
w, h, b = map(int, input().split())

ans = (w * h * b) / (8 * 1024 * 1024)
print("{:.2f}".format(ans), "MB")
