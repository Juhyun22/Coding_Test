# 나의 풀이
def solution(bin1, bin2):
  answer = ''
  a = '0b' + bin1
  b = '0b' + bin2
  sum = int(a, 2) + int(b, 2)
  lsum = list(bin(sum))
  return ''.join(lsum[2:])

# 다른 사람 풀이
def solution(bin1, bin2):
  answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
  return answer
