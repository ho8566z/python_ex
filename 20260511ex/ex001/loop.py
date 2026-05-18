# 반복문(for문 & while문)

# for문: ~하는 동안(지정된 횟수에 따라 반복 -> 횟수 반복)

'''
for 변수 in 반복되는 범위:
    실행구문
'''
'''
#1~10까지의 정수 출력(1, 3, 5, 7, 9, )
#range: 범위지정 함수
#for 변수 in range(시작값, 끝값, 단계):
#끝값(10까지면 11로 입력 / ex: range(1, (n+1), 1))
for num in range(1, 11, 2):
    #실행구문
    print(f'{num} : hello')
'''    

'''
# 0부터 10까지의 정수를 출력
for num in range(0, 11, 1):
    print(f'num: {num}')

#range() <-간략화(단계가 1인 경우에만, 단계를 생략할 수 있다)
for num in range(0, 11):
    print(f'num: {num}')

#range() <-간략화(단계가 생략되고, 시작이 0이면 시작도 생략할 수 있다)
for num in range(11):   #== range(0, 11, 1)
    print(f'num: {num}')
'''

'''
# quiz - 2에서 8까지의 짝수를 출력하자
for num in range(2, 9, 2):
    print(f'num: {num}')
'''
'''
for num in range(1, 16):
    if num < 9:
        if num % 2 == 0:
            print(f'num: {num}')

for num in range(1, 16):
    if (num < 9) and (num % 2 == 0):
        print(f'num: {num}')
'''

'''
#quiz - 사용자가 입력한 횟수만큼 '메일 발송!' 문자열 출력하기
num = int(input(f'메일을 보낼 횟수를 입력하세요. '))
for mail in range(num):     #0~5: 0,1,2,3,4 = 5번
    print('메일발송')
#0부터 시작해야, 원하는 횟수만큼 출력 가능함
'''

'''
#quiz - 1과 10 사이의 정수를 출력할때, 정수가 3의 배수이면 '3의 배수'라고 출력하기
for num in range(1, 11):
    if num % 3 == 0:
        print(f'num: {num} 3의 배수')
    else:
        print(f'num: {num}')

for i in range(1, 11):
    print('3의 배수!' if (i % 3 == 0) else i)
'''

'''
#quiz - 사용자가 원하는 구구단을 입력하면, 해당 구구단을 출력하자
num = int(input(f'원하는 구구단을 입력하세요. '))
for gugu in range(1, 10):
    userGugu = f'{num} x {gugu} = {num * gugu}'
    print(userGugu)

num = int(input(f'원하는 구구단을 입력하세요. '))
for gugu in range(10):
    if gugu != 0:
        userGugu = f'{num} x {gugu} = {num * gugu}'
        print(userGugu)
'''

'''
#quiz - 1부터 10까지의 정수의 합 출력하기
ab = int(input('정수 입력: '))
sum = 0
for num in range(1, ab, 1):
    sum += num
print(f'1부터 {ab}까지 정수의 합:', sum)
'''

'''
#quiz - for문을 이용해서 1~100까지의 정수 중에서 3과 7의 공배수와 최소공배수를 출력하자
miniNum = True
for num in range(1, 101):
    if (num % 3 == 0) and (num % 7 == 0) and miniNum == True:
        print(f'3과 7의 최소공배수: {num}')
        miniNum = False
    elif (num % 3 == 0) and (num % 7 == 0):
        print(f'3과 7의 공배수: {num}')

miniNum = 0
for num in range(1, 101):
    if (num % 3 == 0) and (num % 7 == 0):
        print(f'3과 7의 공배수: {num}')
        if miniNum == 0: miniNum = num
print(f'3과 7의 최소공배수: {miniNum}')
'''

# range() 함수 정리
# for문에서 활용되며, 3개의 데이터가 필요하다(시작, 끝, 단계)
# range(1, 11, 1) = 1에서 10(11-1)까지 1단계씩 증가함
# 시작과 단계 데이터는 생략가능하며, 메모리는 생략한 시작데이터는 
# 0부터 시작하는 것으로, 단계데이터는 1씩 증가하는 것으로 인식함

# 문자열을 이용한 for문
# iterable에는 문자열도 이용 가능함
'''
for word in 'H e l l o':
    print(f'word: {word}')
'''
# word: H
# word:  
# word: e
# word:  
# word: l
# word:  
# word: l
# word:  
# word: o

'''
#quiz - 사용자가 원하는 구구단을 입력하면, 해당 구구단을 출력하자
num = int(input(f'원하는 구구단을 선택하세요. '))
for gugu in range(1, 10):
    print(f'{num} x {gugu} = {num * gugu}')
'''



# while문: ~하는 동안(특정조건에 의한 반복 -> 조건 반복)
# 조건식의 결과가 참인 경우, 실행문을 계속해서 반복함
'''
num = 0
while num < 5:
    print(num)
    num += 1
'''
'''
# wfile "num < 5": (<- "num < 5": 조건식)
num = 1

while num <= 10:
    print(f'num: {num}')
    num += 1
'''

'''
#quiz - 1부터 30까지의 정수 중 홀수와 짝수를 구분해 출력하기
num = 1

while num < 31:

    if num % 2 == 0:
        print(f'{num}은 짝수')
    else:
        print(f'{num}은 홀수')
    
    num +=1
'''

'''
#quiz - 구구단 3단 출력하기
num = 3

while num < 4:
    for gugu in range(1, 10):
        print(f'{num} x {gugu} = {num * gugu}')
    
    num += 1

num = 1
while(num < 10):
    print(f'3 x {num} = {3 * num}')
    num += 1
'''

'''
#quiz - 구구단 전체 출력하기
num1 = 2
while num1 < 10: 
    num2 = 1
    while num2 < 10:
        print(f'{num1} x {num2} = {num1 * num2}')
        num2 += 1
    num1 += 1
'''

'''
# # #quiz - 구구단 출력하기(2)
num1 = 2
while num1 < 10:
    num2 = 1
    while num2 < 10:
        print(f'{num1}x{num2}={num1 * num2}\t', end="|")
        num2 += 1
    print()
    num1 += 1

num1 = 1
while num1 < 10:
    num2 = 2
    while num2 < 10:
        print(f'{num2}x{num1}={num2 * num1}\t', end="|")
        num2 += 1
    print()
    num1 += 1
'''

# num1 = 1
# while num1 < 10:

#     num2 = 2
#     str = ''
#     while num2 < 10:
#         str += f'{num2}x{num1}={num2 * num1}\t'
#         num2 += 1
    
#     print(str)
#     num1 += 1

'''
#quiz - while문과 if문을 활용해 0에서 100까지의 정수 중에서 3과 8의 공배수, 최소공배수 구하기
num1 = 1
num2 = 0

while num1 <= 100:
    if num1 % 3 == 0 and num1 % 8 ==0:
        print(f'3과 8의 공배수: {num1}')
        if num2 == 0:
            num2 = num1
    num1 += 1
print(f'3과 8의 최소공배수: {num2}')
'''


# 반복문 내 실행 제어(continue, break)

# continue: 
# 반복문에서 continue 키워드를 사용하면 이후 실행을 생략하고 다시 반복문의 처음으로 돌아간다
'''
# continue를 활용해 1부터 10까지의 정수 중 홀수만 출력하는 프로그램
# (continue 사용x)
for num in range(1,11):
    if num % 2 == 1:
        print(f'num: {num}')

# (continue 사용)
for num in range(1,11):
    if num % 2 == 0:
        continue
    print(f'num: {num}')
'''


# break:
# 반복문에서 break 키워드를 만나면 '실행을 중단하고 반복문응 빠져' 나온다
'''
#1부터 10까지의 정수를 더하되, 결과가 30이상이 될 때, 정수를 찾는 프로그램

num1 = 1
num2 = 0
while num1 < 11:
    num2 += num1
    if num2 >= 30:
        print(f'num1: {num1}')
        break
    num1 += 1
'''

'''
# pass키워드
for num in range(1, 10):
    pass    #TERMINAL에서 '에러'로 인해 작동하는 것을 막기 위함
'''

'''
# quiz - 삼각형의 넓이 구하기
# 가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램
# 단, 가로길이는 1부터 2의 배수로 증가하고, 세로길이는 1부터 3의 배수로 증가함
# 삼각형의 넓이가 150보다 크면 프로그램 종료

cnt = 1
maxArea = 150
while True:
    result = ((cnt * 2) * (cnt * 3)) / 2
    if result > 150: break
    print(f'삼각형의 넓이는? {result}')
    cnt += 1
'''
