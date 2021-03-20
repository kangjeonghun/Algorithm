# 코드업 기초 100제
# 기본 문법정리

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

#chr( ) 확장 : 문자 1개를 입력받고 다음 문자 출력
a = input()
print(chr(a+1)) # 아스키코드에서 a = 65를 의미하므로 파라미터 내부가 66으로 읽혀짐

# 거듭제곱 연산자 (float형도 가능)
a,b = input().split()
c = int(a)**int(b)
print(c)

# a를 b로나눈 몫과 나머지 구하기
print(a // b) # 몫
print(a % b) # 나머지

# 반올림 round함수
f = 10.112
round(f, 2) # 10.11이 출력됨

# round 심화  

# 소숫점 둘째자리 이상 불필요한 0이 있는 경우 출력되지 않는다.
#round(x,2) 결과가 5.67인 경우 5.67 이 출력됨.
#round(x,2) 결과가 5.60인 경우 5.6 만 출력됨.
#round(x,2) 결과가 5.00인 경우 5.0 만 출력됨. 

# 실수 2개를 입력받아 나눈 결과 계산 (출력 소수 셋째짜리까지)
f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print('%.3f' %(f1/f2)) # 출력시 %.?f꼴로 출력하면 ?+1번째에서 반올림하여 출력함.

# 정수 3개 입력받아 합과 평균 출력
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a+b+c,round(a+b+c/3,2))

# 비트 시프트 이용, 정수 1개 입력받아 2배 곱해 출력
# 1/2는 >>1 , 10진수를 2진수 변환했을때, 0을 왼쪽맨끝에 밀어넣는다고 생각
n = int(input())
print(n<<1)
# python에서 실수 값에 대한 비트시프트 연산은 허용되지 않고 오류가 발생한다.
# (실수 값도 컴퓨터 내부적으로는 2진수 형태로 저장되고 비트시프트 처리가 될 수 있지만, python 에서는 허용하지 않는다.)
# n = 10.0 으로 작성해 넣으면 자동으로 실수 값으로 저장된다.
# n = 0o10 으로 작성해 넣으면 8진수(octal) 10으로 인식되어 10진수 8값이 저장되고,
# n = 0xf 나 n = 0XF 으로 작성해 넣으면 16진수(hexadecimal) F로 인식되어 10진수 15값으로 저장된다

# 2의 거듭제곱 배로 곱한 후 출력하기
a,n = input().split()
a = int(a)
n = int(n)
print(a<<n) # a * 2^n 한 결과가 나옴

#================================6000~6051=================

# 정수를 입력받고 반대의 bool값 계산하기
a = bool(int(input()))
print(not a)

# 기초 비트단위 논리연산 : ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),<<(bitwise left shift), >>(bitwise right shift)
# 1. bitwise not(~)
a = 1
print(~a) # -2가 출력됨
# 1은 32비트 2진수 표현시 00000000 00000000 00000000 00000001로 표현되는데
# 여기에 ~를 붙이면 11111111 11111111 11111111 11111110 이다. 이는 -2를 의미함
# 그럼 -1은? 32비트가 전부 1인경우이고, 0은 32비트가 전부 0인 경우이다.
# 간단정리 : ~n = -n - 1

# 2. bitwise and(&)
print(3 & 5) # 32비트의 2진수로 표현했을 때, and에 엮이는 부분이 맨끝자리밖에 없으므로 1출력

# 3. bitwise or(|), bitwise xor(^) 생략
# 이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용된다.

# 간단한 3항연산
# a = b if c>d else e => 만약 c>d라면 b를 a에 저장하고, false이면 e를 a에 저장함.

# 알파벳 입력받고 카운트다운
c = ord(input())
t = ord('a')
while c>=t:
    print(chr(t), end='')
    t += 1
# 이때, print(..., end=..) 꼴은 while문을 돌때 개행을 하지 않고, 값 출력 후 공백문자 ''를 출력

# 16진수 구구단?
ans = input()
ans = int(ans, 16)
i = 0
while i < 15:
    print('%X * %X = %X'%(ans, i+1, ans*(i+1) ))
    i += 1

# range(시작, 끝, 증감) #시작 수는 포함, 끝 수는 포함하지 않음. [시작, 끝)
# range(n-1, -1, -1) #n-1, n-2, ..., 3, 2, 1, 0

# List Comprehensions
# 20x20의 리스트 d 생성 , 모든 성분은 0
# d = [[0 for j in range(20)] for i in range(20)]
'''d=[]
 for i in range(20) :
  d.append([])
  for j in range(20) :
    d[i].append(0)
와 같은 역할'''
#===================6000~6096============================
