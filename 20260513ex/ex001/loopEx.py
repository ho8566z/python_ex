# # quiz - 3,6,9 게임만들기
# '''
# 1부터 99까지 1씩 증가하면서 숫자에 3,6,9가 들어있을 때마다 숫자와 함께
# '짝'을 출력하자
# 3 -> '짝'
# 33 -> '짝짝'
# '''

# for num in range(1, 100):

#     if num <= 9:                    #1의 단위
#         if num % 3 == 0:
#             print(f'{num},짝')
#         else:
#             print(f'{num}')
                                
#     else:                          #10의 단위
#         # print(f'{num}')          #12-> 1,2 / 37-> 3,7 / 66-> 6,6
#         no = str(num)
#         firstNum = num // 10       #15-> 15 // 10-> 1
#         secondNum = num % 10       #15-> 15 % 10-> 5

#         if firstNum % 3 == 0:
#             # print(f'짝')
#             no += ',짝'
        
#         if secondNum % 3 == 0 and secondNum != 0:
#             # print(f'짝')
#             no += ',짝'

#         print(f'{no}')


# for num in range(1, 100):

#     if num <= 9:                    #1의 단위
#         if num % 3 == 0:
#             # print(f'{num},짝')
#             print(num, ', 짝', end='')
#         else:
#             print(num, end='')
                                
#     else:                          #10의 단위
#         # print(f'{num}')          #12-> 1,2 / 37-> 3,7 / 66-> 6,6
#         # no = str(num)
#         print(num, end='')

#         firstNum = num // 10       #15-> 15 // 10-> 1
#         secondNum = num % 10       #15-> 15 % 10-> 5

#         if firstNum % 3 == 0:
#             # print(f'짝')
#             # no += ',짝'
#             print(',짝', end='')
        
#         if secondNum % 3 == 0 and secondNum != 0:
#             # print(f'짝')
#             # no += ',짝'
#             print(',짝', end='')

#     print()


# quiz - 열차 교차시간 파악하기
'''
대전역에는 3개 노선의 열차가 오전9시부터 오후6시까지 교차운행한다
3대의 열차가 교차하는 시간을 구해 열차 충돌을 막자
(단, 매일 오전9시에 대전역에서 모든 열차가 출발한다)

a열차: 첫차 오전9시, 마지막 오후6시, 운행간격 10분
b열차: 첫차 오전9시, 마지막 오후6시, 운행간격 25분
c열차: 첫차 오전9시, 마지막 오후6시, 운행간격 30분

ab: 50분, ac: 30분, bc: 300분(5시간)
'''

trainA = 10
trainB = 25
trainC = 30

# for time in range(1, 541):
#     if time % trainA == 0 and time % trainB == 0 and time % trainC == 0:
#         print('trainA <-> trainB <-> trainC: ', end='')
#         print(9 + time // 60, end='')               #시(시각)
#         print('시', end='')
#         print(time % 60, end='')
#         print('분')

#     elif time % trainA == 0 and time % trainB == 0:
#         print('trainA <-> trainB: ', end='')
#         print(9 + time // 60, end='')               #시(시각)
#         print('시', end='')
#         print(time % 60, end='')
#         print('분')

#     elif time % trainA == 0 and time % trainC == 0:
#         print('trainA <-> trainC: ', end='')
#         print(9 + time // 60, end='')               #시(시각)
#         print('시', end='')
#         print(time % 60, end='')
#         print('분')

#     elif time % trainB == 0 and time % trainC == 0:
#         print('trainB <-> trainC: ', end='')
#         print(9 + time // 60, end='')               #시(시각)
#         print('시', end='')
#         print(time % 60, end='')
#         print('분')

# for time in range(1, 541):
#     if time % trainA == 0 and time % trainB == 0 and time % trainC == 0:
#         print('trainA <-> trainB <-> trainC: ', end='')
#         print(9 + time // 60, end='')               #시(시각)
#         print('시', end='')
#         print(time % 60, end='')
#         print('분')

# for time in range(1, 541):
#     if time % trainA == 0 and time % trainB == 0 and time % trainC == 0:
#         print('trainA <-> trainB <-> trainC: ', end='')
#         print(f'{9 + time // 60}시 {'00' if time % 60 == 0 else str(time % 60)}분')


#     elif time % trainA == 0 and time % trainB == 0:
#         print('trainA <-> trainB: ', end='')
#         timeSet = '0' if time % 60 == 0 else time
#         print(f'{9 + time // 60}시 {'00' if time % 60 == 0 else str(time % 60)}분')

#     elif time % trainA == 0 and time % trainC == 0:
#         print('trainA <-> trainC: ', end='')
#         timeSet = '0' if time % 60 == 0 else time
#         print(f'{9 + time // 60}시 {'00' if time % 60 == 0 else str(time % 60)}분')

#     elif time % trainB == 0 and time % trainC == 0:
#         print('trainB <-> trainC: ', end='')
#         timeSet = '0' if time % 60 == 0 else time
#         print(f'{9 + time // 60}시 {'00' if time % 60 == 0 else str(time % 60)}분')


# quiz - 로그인 기능 만들기
'''
시스템 관리자(administrator) 로그인 기능을 만들어 보자
관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렸다면'암호를 다시 확인하세요!'를 출력하고
다시 암호를 물어봅니다. 
5회 이상 로그인에 실패하면 '로그인 실패!! 횟수 초과!!!' 메시지를 출력하고 종료합니다.
암호가 올바르다면 '로그인 됐습니다.'를 출력하고 종료합니다. 올바른 암호는 'dwac1234'입니다.
'''

# ADMIN_PW = 'dwac1234'
# cnt = 1
# while True:

#     if cnt > 5:
#         print(f'암호 입력 실패 - 입력횟수 초과')
#         break

#     inputPw = input(f'관리자 암호입력: ')

#     if inputPw != ADMIN_PW:
#         print(f'암호 입력 실패 - 재입력: ')
#         cnt += 1
    
#     elif inputPw == ADMIN_PW:
#         print(f'암호 입력 성공')
#         break


# quiz
'''
사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램을 만들어라
팩토리얼(factorial, !) n!은 1부터 양의 정수 n까지의 모든 정수를 곱한 값이다
(예를 들어, 4!은 1x2x3x4 = 24이다)
'''

# userInputIntegerData = int(input(f'양수 입력: '))
# result = 1
# for num in range(1, userInputIntegerData + 1):
#     result *= num
# print(f'{userInputIntegerData}의 팩토리얼은 {result}이다')


# quiz - 숫자 맞추기 게임
'''
0부터 100사이의 난수를 발생시키고 사용자가 난수를 맞출 때까지 계속해서 물어보는 게임
다음은 프로그램 개발에 필요한 요구사항이다

요구사항
-1부터 100까지의 난수를 발생시킴
-사용자가 입력한 숫자가 난수와 일치하면 '정답'을 출력하고 게임을 종료
-사용자가 입력한 숫자가 난수와 일치하지 않으면 '오답'을 출력하고, 다시 질문
-기회는 10회로 제한하고, 만약 10번을 넘으면 '게임 실패'를 출력하고 게임을 종료
-사용자가 틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다
-마지막으로, 게임을 종료하기 전에 난수를 출력한다
'''

# import random
# randomNum = random.randint(1, 100)
# cnt = 0

# while True:

#     userNum = int(input('숫자 입력: '))    
#     cnt += 1

#     if userNum == randomNum:
#         print(f'정답')
#         break

#     elif cnt >= 10:
#         print(f'오답')
#         break

#     elif randomNum < userNum:
#         print(f'입력한 숫자 {userNum}는 난수보다 크다')

#     elif randomNum > userNum:
#         print(f'입력한 숫자 {userNum}는 난수보다 작다')

# print(f'정답: {randomNum}')


# quiz - 다음 요구조건을 참고해 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램
'''
-가로길이는 1부터 2의 배수로 증가
-세로길이는 1부터 3의 배수로 증가
-사각형의 넓이가 150보다 크면 프로그램 종료
-가장 작은 사각형과 가장 큰 사각형의 넓이를 출력
'''

# # 초기값
# width = 1
# height = 1

# # 가장 작은 사각형 넓이
# minArea = width * height
# # 가장 큰 사각형 넓이
# maxArea = width * height

# while True:

#     area = width * height   #사각형 넓이

#     if area > 150:
#         break

#     print(f'가로: {width}, 세로: {height}, 넓이: {area}')

#     if area < minArea:  #최소 넓이
#         minArea = area 

#     if area > maxArea:  #최대 넓이
#         maxArea = area

#     if width == 1:      #width가 1인 경우
#         width = 2
#     else:               #width가 1이 아닌 경우
#         width += 2

#     if height == 1:
#         height = 3
#     else:
#         height += 3

# print(f'가장 작은 넓이: {minArea}')
# print(f'가장 큰 넓이: {maxArea}')
