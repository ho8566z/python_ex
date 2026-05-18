# num1 = 100
# num2 = 10
# print(f'num1 / num2 = {num1 / num2}')   #num1 / num2 = 10.0

# nop1 = 90
# nop2 = 3
# print(f'nop1 / nop2 = {nop1 / nop2}')   #nop1 / nop2 = 30.0

# print(0 / 111)  #0.0
# print(111 / 0)  #ZeroDivisionError: division by zero

# print(10 % 4)   #2
# print(10 % 5)   #0

# inputData = int(input('~?'))
# result = inputData % 2
# print(result)

# print(10 // 2)  #5
# print(10 // 6)  #1

# pen = 200
# penCnt = 6
# maxPeopleCnt = pen // penCnt
# print(f'받을 수 있는 사람 수: {maxPeopleCnt}')
# #받을 수 있는 사람 수: 33

# restPenCnt = pen % penCnt
# print(f'남는 pen의 개수: {restPenCnt}')
# #남는 pen의 개수: 2

# print(3 ** 3)   #27
# print(3 ** 6)   #729
# print(3 ** 9)   #19683

# people = 3
# date = 9
# total = people ** date
# print(f'{date}일 이후, 사람 수: {total}')
# #9일 이후, 사람 수: 19683

# nop = 10
# nop = nop + 5

# # 10년 만기, 복리 예금, 10만원 입금
# myAssets = 5000000
# rate = 0.1

# #(1~)10년 이후 총 수령액
# myAssets = myAssets + (myAssets * rate)
# print(f'10년 이후, 총 수령액: {int(myAssets):,}원')
# #10년 이후, 총 수령액: 5,500,000원

# nop1 = ' '; nop2 = '0'
# print(nop1 == nop2)
# print(nop1 != nop2)

# print(nop1 > nop2)
# print(nop1 >= nop2)

# print(nop1 < nop2)
# print(nop1 <= nop2)

# va1 = True; va2 = True; va3 = False
# print(va1 and va2)  #True
# print(va1 and va3)  #False
# print(va2 and va3)  #False

# print(va1 or va2)  #True
# print(va2 or va3)  #True

# va1 = True
# print(not va1)  #False

# va2 = False
# print(not va2)  #True

# nop1 = 10; nop2 = 20; nop3 = 30
# result = (nop1 < nop2) and (nop2 < nop3)
# print(f'result: {result}')  #result: True

# nop1 = 10; nop2 = 20; nop3 = 30
# result = (nop1 > nop2) and (nop2 < nop3)
# print(f'result: {result}')  #result: False

# nop1 = 10; nop2 = 20; nop3 = 30
# result = (nop1 > nop2) and (nop2 > nop3)
# print(f'result: {result}')  #result: False

# result = (nop1 < nop2) and (nop2 < nop3) and (nop3 > nop1)
# print(f'result: {result}')  #result: True

# height = float(input('신장을 입력하세요.'))
# result = (height >=120) and (height <= 175)
# print(f'result: {result}')

# weight = float(input('체중을 입력하세요.'))
# result = (weight >= 30) and (weight <= 65)
# print(f'result: {result}')

# nop1 = 10           #이항 연산자
# nop1 = 10 + 10      #이항 연산자
# not True            #단항 연산자

# targetWeight = 75
# myWeight = 93
# result = '성공' if myWeight <= targetWeight else '실패'
# print(f'result: {result}')  #result: 실패

# targetWeight = float(input('목표 체중을 입력하세요.'))  #78
# myWeight = float(input('현재 체중을 입력하세요.'))      #93
# result = '대단해요' if myWeight <= targetWeight else '노력하세요'
# print(f'result: {result}')  #result: 노력하세요


print('----------------------------------------------')
print('--------------------260508--------------------')
print('----------------------------------------------')

targetLength = 180
print('기준 신장: 175')    #기준 신장: 175
myLength = float(input('당신의 신장: '))   #당신의 신장: 180
result = '가능' if targetLength <= myLength else '불가능'
print(f'result: {result}')    #result: 가능
