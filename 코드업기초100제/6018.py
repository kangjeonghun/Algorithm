# 코드업 기초 100제

# 시간:분 형태를 입력받고, 출력까지 하는 코드
a, b = input().split(':') # ':'을 기준으로 a, b를 나눔
print(a, b, sep=':') # ':'을 사이에 두고 출력 되도록함

# 년,월,일을 입력받고 역으로 출력
y,m,d = input().split('.')
print(y,m,d, sep = ('-'))

# 주민등록번호(앞-뒤)를 입력받고 '-'없이 출력하기
front,back = input().split('-') # 앞과 뒤를 구분지어 입력받음
print(front+back) # input은 문자열로 인식하기에'+'로 처리해줌

# 문자열 입력받고 알파벳 하나씩 개행하여 출력
str = input()
for i in range(len(str)): # 입력받은 문자열의 길이만큼 반복문 실행
	print(str[i])

# 주민등록번호 앞자리 입력받고 년,월,일 각각 2개씩 쪼개기
front = input()
print(front[0:2],front[2:4],front[4:6])

# 시,분,초 입력받아 분만 출력하기(입력 형태 시:분:초)
h,m,s = input().split(':')
print(m)

# 두 실수를 입력받아 합연산 후 출력
a,b = input().split(' ')
print(float(a) + float(b))

# 10진수 형태의 수 입력받고 16진수(hexademical) 변환
a = input()
n = int(a)
print('%x'%n) #이때 %x를 %X로 쓰면 대문자형태의 16진수 출력

# 16진수 형태의 수 입력받고 8진수(octal) 변환
a = input()
n = int(a, 16) # 문자열a를 16진수로 변환하여 n에 저장
print('%o'%n) # n을 8진수로 변환하여 출력

# 알파벳 입력받아서 10진수 유니코드로 출력
# 유니코드 : 세계 여러 나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준 코드
# ord( ) 는 어떤 문자의 순서 위치(ordinal position) 값을 의미한다.  
# 실제로 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여 되어 있다. A:65, B:66, C:67 .... 
# ord(c) : 문자 c 를 10진수로 변환한 값 
n = ord(input())
print(n)

# chr( )는 정수값->문자, ord( )는 문자->정수값 형태로 바꿔줌
# 이때 입력값은 32~126범위를 입력함.
n = int(input())
print(chr(n))


