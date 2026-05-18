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

'''
import random
randomNum = random.randrange(1, 100)
cnt = 0

while True:

    userNum = int(input('1부터 100까지의 숫자 중에 입력: '))
    cnt += 1

    if randomNum == userNum:
        print(f'정답')
        break

    elif cnt >= 10:
        print(f'실패')
        print(f'게임 종료')
        break

    elif randomNum < userNum:
        print(f'입력한 숫자 {userNum}은 난수보다 크다')
    
    elif randomNum > userNum:
        print(f'입력한 숫자 {userNum}은 난수보다 작다')    

print(f'정답: {randomNum}')
'''



# quiz - 다음 요구조건을 참고해 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램
'''
-가로길이는 1부터 2의 배수로 증가
-세로길이는 1부터 3의 배수로 증가
-사각형의 넓이가 150보다 크면 프로그램 종료
-가장 작은 사각형과 가장 큰 사각형의 넓이를 출력
'''

'''
width = 1
height = 1
# minArea = width * height
# maxArea = width * height

while True:
    
    area = width * height

    if area > 150:
        break
    
    print(f'가로길이: {width}, 세로길이: {height}, 사각형 넓이: {area}')

    if area < minArea:
        minArea = area
    
    if area > maxArea:
        maxArea = area
    
    if width == 1:
        width = 2
    else:
        width += 2

    if height == 1:
        height = 3
    else:
        height += 3

print(f'가장 작은 사각형의 넓이: {minArea}')
print(f'가장 큰 사각형의 넓이: {maxArea}')
'''

# quiz - 합격 여부 판단하기
'''
다음은 홍길동 수험생의 2020년 공인중개사 자격증 시험 성적표입니다.
아래 합격 기준에 만족하는지 구하는 프로그램을 만들어봅시다.
 - 매 과목 100점을 만점으로 하여 매 과목 40점 이상
 - 전 과목 평균 60점 이상 득점

 홍길동 수험생 성적표
 부동산 개론: 55점
 민법: 35점
 공법: 40점
 공시법: 70점
 세법: 65점
 중개사법: 30점
'''

# scores = [55, 35, 40, 70, 65, 30]

# total = 0
# underScoreSbject = 0
# average = 0

# for score in scores:
#     if score < 40:
#         underScoreSbject += 1
        
#     total += score
    
# print(f'과목 40점 이하: {underScoreSbject}개')

# average = total / len(scores)
# print(f'과목 평균: {average:.2f}점')

# if underScoreSbject > 0 or average < 60:
#     print(f'다음기회')
# else:
#     print(f'축하')
# # 과목 40점 이하: 2개
# # 과목 평균: 49.17점
# # 다음기회



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
# randomNumber = random.randrange(1, 101)

# userNumber = int(input(f'숫자 입력: '))
# flag = True
# cnt = 0

# while flag:
#     if cnt < 10:
#         if userNumber < randomNumber:
#             print(f'입력한 숫자: {userNumber}는 난수보다 작다')
#         elif userNumber > randomNumber:
#             print(f'입력한 숫자: {userNumber}는 난수보다 크다')
            
#         print(f'숫자 재입력:')
#         cnt += 1
    
#         flag = False
#         print(f'기회 10번 종료')

# if userNumber == randomNumber:
#     print(f'정답')


import random
randomNumber = random.randrange(1, 101)
cnt = 0

while True:
    userNumber = int(input(f'숫자 입력: '))
    cnt += 1

    if userNumber == randomNumber:
        print(f'정답')
        break

    elif cnt >= 10:
        print(f'오답')

    elif userNumber < randomNumber:
        print(f'입력한 숫자: {userNumber}는 난수보다 작다')

    elif userNumber > randomNumber:
        print(f'입력한 숫자: {userNumber}는 난수보다 크다')
            
print(f'정답: {randomNumber}')