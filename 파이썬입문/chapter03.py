# 실습 문제
# 1.
n = int(input('정수 입력>> '))
print('2진수로 변환 =>', bin(n))
print('8진수로 변환 =>', oct(n))
print('16진수로 변환 =>', hex(n))

# 2.
s = input('문자열 입력>> ')
w1 = input('찾을 단어>> ')
w2 = input('바꿀 단어>> ')
print('{:-^5}'.format('결과'))
print(s[:s.index(w1)], w2, s[s.index(w1)+len(w1):])

# 5.
nums = input('주민 번호를 -를 포함해서 입력하라>> ')
print('주민 번호 앞자리 :', nums[:nums.index('-')])
print('주민 번호 뒷자리 첫 글자 :', nums[nums.index('-')+1])