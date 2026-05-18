#quiz - 사용자가 원하는 구구단을 입력하면, 해당 구구단을 출력하자
# gugu = int(input(f'구구당 숫자 입력: '))
# for num in range(1, 10):
#     print(f'{gugu}x{num}={gugu*num}')


#quiz - 1부터 10까지의 정수의 합 출력하기
# sum = 0
# for num in range(1, 11):
#     sum += num
# print(f'정수의 합: {sum}')


#quiz - for문을 이용해서 1~100까지의 정수 중에서 3과 7의 공배수와 최소공배수를 출력하자
# num1 = 0
# for num2 in range(0, 101):
#     if num2 % 3 == 0 and num2 % 7 == 0:
#         print(f'3과 7의 공배수: {num2}')
#     elif num1 == 0: num1 = num2
# print(f'3과 7의 최소공배수: {num1}')


#quiz - 구구단 3단 출력하기
# num1 = 1
# while num1 < 10:
#     print(f'3x{num1}={3*num1}')
#     num1 += 1


#quiz - 구구단 전체 출력하기
# num1 = 2
# while num1 < 10:
#     num2 = 1
#     while num2 < 10:
#         print(f'{num1}x{num2}={num1*num2}')
#         num2 += 1
#     num1 += 1


#quiz - 구구단 전체 출력하기(가로)
# num1 = 2
# while num1 < 10:
#     num2 = 1
#     while num2 < 10:
#         print(f'{num1}x{num2}={num1*num2}\t',end="|")
#         num2 += 1
#     print()
#     num1 += 1


#quiz - while문과 if문을 활용해 0에서 100까지의 정수 중에서 3과 8의 공배수, 최소공배수 구하기
# num1 = 1
# num2 = 0
# while num1 < 100:
#     if num1 % 3 == 0 and num1 % 8 == 0:
#         print(f'3과 8의 공배수: {num1}')
#         if num2 == 0:
#             num2 = num1
#     num1 += 1
# print(f'3과 8의 최소공배수: {num2}')


#quiz - for문을 이용해서 1~100까지의 정수 중에서 3과 7의 공배수와 최소공배수를 출력하자
num1 = 0
for num2 in range(1, 101):
    if (num2 % 3 == 0) and (num2 % 7 == 0):
        print(f'3과 7의 공배수: {num2}')
        if num1 == 0: num1 = num2
print(f'3과 7의 최소공배수: {num1}')
