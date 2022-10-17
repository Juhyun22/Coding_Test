# 어떤 식으로 출력되는지 잘 확인!!
h, b, c, s = map(int, input().split())

ans = (h * b * c * s) / (8 * 1024 * 1024)
ans = round(ans, 1)

print(ans, "MB")
