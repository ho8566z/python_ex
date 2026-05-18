# print('회원정보를 입력하세요.')

# userName = input('이름: ')
# userMail = input('메일: ')
# userID = input('아이디: ')
# userPW = input('비밀번호: ')
               

# print('------------------------------------')
# print('To. ' + userMail) #userMail은 문자열이 아닌, 변수명으로 인식되어 출력
# print('▶ 아이디 및 비밀번호 확인')
# print(userName + ' 고객님 안녕하세요.')
# print(userName + ' 고객님의 아이디와 비밀번호는 다음과 같습니다.')
# print('ID : ' + userID)
# print('PW : ' + userPW)
# print('감사합니다.')
# print('NAVER 담당자.')
# print('------------------------------------')

# userMail = 'gildong@gmail.com'
# print('To. gildong@gmail.com')
# print('To. ' + userMail)
# print('To. ', userMail)

# print('------------------------------------')
# print("이름:", "홍길동", "나이:", "20") #print("이름:", "홍길동", "나이:", "userAge")

# print('------------------------------------')
# print("2026", "05", "06", sep="-") #sep는 2026,05,06 사이를 '-'로 구분하겠다는 함수

# print('------------------------------------')
# print("hello", end="     ")
# print("world")

# print('------------------------------------')
# f-string (무조건 필수)
# name = "철수"
# age = 25

# print('이름은 ' + name + ', 나이는 ' + str(age) + '입니다.')
# print(f'이름은 {name}, 나이는 {age}입니다.') #에러, 오타를 줄일 수 있는 가장 최선

# #format() (무조건 필수2)
# print("이름은 {}, 나이는 {}입니다.".format(name, age))

# print("이름은 {1}, 나이는 {0}입니다.".format(age, name)) #숫자시작은 0부터, 사용량 저조 = 인덱스번호

# korScore = input('국어 점수')
# engScore = input('영어 점수')
# matScore = input('수학 점수')

# print(f'국어 점수 : {korScore}')
# print(f'영어 점수 : {engScore}')
# print(f'수학 점수 : {matScore}')

# print('------------------------------------')

# firstNum = int(input('첫 번째 정수 입력: '))
# secondNum = int(input('두 번째 정수 입력: '))

# sum = firstNum + secondNum
# average = sum / 2

# print(f'합: {sum}')
# print(f'평균: {average}')

# print(f'합: {firstNum + secondNum}')
# print(f'평균: {(firstNum + secondNum) / 2}')


# var1 = 10
# var2 = 20
# print(f'var1: {var1}, var2 {var2}')

# temp = var1
# var1 = var2
# var2 = temp
# print(f'var1: {var1}, var2 {var2}')


num1 = 2 ** 4
print(num1)

print(2 ** 2)
print(2 ** 4)