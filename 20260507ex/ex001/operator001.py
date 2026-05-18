# 나눗셈 연산자 "/"

# print(10 / 2)   #5.0
# print(3.14 / 0.5)   #6.28
# print(3.14 / .5)    #6.28

# num1 = 100
# num2 = 10
# print(f'num1 / num2 = {num1 / num2}')   #10.0

#quiz - BMI

# weight = float(input('몸무게를 입력하세요(kg): '))
# height = float(input('신장을 입력하세요(m): '))
# bmi = weight / (height * height)
# print(f'BMI: {bmi:}')
# print(f'BMI: {bmi:.2f}')

# # 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다
# print(0 / 122)  #0.0

# # 어떤 숫자를 0으로 나눌 수 없다 #에러
# print(122 / 0)  #ZeroDivisionError

# 나머지, 몫, 거듭제곱
# print(10 % 2)   # 0 (나머지 '%')
# print(10 % 3)   # 1 (나머지 '%')

# # 짝수는 0, 홀수는 1을 출력
# inputData = int(input('손 안에 동전의 개수를 입력하세요.'))
# result = inputData % 2
# print(result)

# 몫 "//"
# print(10 // 3)  # 3
# print(1187 // 3)   # 395

# # quiz
# # 97개의 빵을 3개씩 나누어 줄 때, 최대 몇명에게 나누어 줄 수 있는지?
# bread = 97
# breadCnt = 3
# maxFriendsCnt = bread //breadCnt
# print(f'빵을 나누어 줄 수 있는 최대 학생 수: {maxFriendsCnt}')

# restBreadCnt = bread % breadCnt
# print(f'남는 빵의 개수: {restBreadCnt}')

# 거듭제곱 "**"
# print(2**2)     #4
# print(2**3)     #8
# print(2**10)    #1024

# # quiz (전염병 예상 감염자 수 구하기)
# # 보건 당국은 전염병의 감염 확산 추세를 파악한 결과,
# # 하루에 1명이 1명을 감염시킴
# # 감염자 1명이 생길 때, 30일 이후에 몇 명으로 확산될것인가?

# man = 2
# date = 30
# total = man ** date
# print(f'{date}일 이후, 예상 감염자 수: {total}')
#     #30일 이후, 예상 감염자 수: 1073741824
