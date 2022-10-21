# [start : end : step] = step 만큼 건너 뛰면서 안의 내용 추출
# 나의 풀이
def solution(cipher, code):
  answer = ''
  list_cipher = list(cipher)
  for i in range(len(list_cipher)):
    if (i + 1) % code == 0:
      answer += str(list_cipher[i])
  return answer

# 다른 사람 풀이
def solution(cipher, code):
  answer = cipher[code -1 : : code]
  return answer
