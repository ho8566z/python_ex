# # 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
# #  [3, 7, 1, 9, 5]

# numbers = [3, 7, 1, 9, 5]
# numbers.sort()
# print(f'numbers: {numbers}')                        #numbers: [1, 3, 5, 7, 9]
# print(f'numbers: {numbers[len(numbers)-1:]}')       #numbers: [9]



# 2. 사용자에게 숫자 입력받아서 1부터 입력한 숫자까지 합계 출력하기
# inputData = []
# userInputData = int(input(f'숫자 입력: '))      #숫자 입력: 10
# print(f'입력한 숫자: {userInputData}')          #입력한 숫자: 10
# inputData.append(userInputData + 1)

# sum = inputData[len(inputData)-1]
# cnt = 0

# for plus in range(1, sum):
#     cnt += plus
# print(f'1부터 입력한 숫자까지의 합: ', cnt)       #1부터 입력한 숫자까지의 합:  55



# 3. 리스트에 있는 숫자 중 짝수만 출력하기
# [1,2,3,4,5,6]
# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     if num % 2 == 0:
#         print(f'numbers의 짝수는: {num}')
# # numbers의 짝수는: 2
# # numbers의 짝수는: 4
# # numbers의 짝수는: 6



# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]
# numbers = [5,1,7,3]
# numbers.sort()
# print(f'numbers: {numbers}')        #numbers: [1, 3, 5, 7]



# 5. 리스트 숫자를 내림차순 정렬하기
# [5,1,7,3]
# numbers = [5,1,7,3]
# numbers.sort(reverse=True)
# print(f'numbers: {numbers}')        #numbers: [7, 5, 3, 1]



# 6. 리스트 안 숫자의 평균 구하기 
# [10,20,30]
# numbers = [10,20,30]
# total = 0
# average = 0

# for number in numbers:
#     total += number
#     average = total / len(numbers)
# print(f'numbers의 평균: {average:.2f}')     #numbers의 평균: 20.00



# 7. 리스트에서 가장 작은 숫자 찾기
# (min() 사용 금지)
# numbers = [3, 55, 16, 1, 12, 63]
# numbers.sort()
# print(f'numbers에서 가장 작은 숫자: {numbers[0]}')    #numbers에서 가장 작은 숫자: 1



# 8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기
# for num in range(1, 100):
#     if num % 3 == 0 and num % 5 == 0:
#         print(f'3과 5의 공배수: {num}')
# # 3과 5의 공배수: 15
# # 3과 5의 공배수: 30
# # 3과 5의 공배수: 45
# # 3과 5의 공배수: 60
# # 3과 5의 공배수: 75
# # 3과 5의 공배수: 90



# # 9. 사용자가 입력한 숫자를 리스트에 저장하다가 0을 입력하면 종료 후 리스트 출력하기
# # [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]
# numbers = []
# flag = True

# while flag:

#     userNum = int(input(f'숫자를 입력하세요. '))
#     numbers.append(userNum)
#     print(f'입력한 숫자는? {userNum}')
#     if userNum == 0:
#         print(f'0을 입력해 종료합니다. ')
#         print(f'입력한 숫자 목록: {numbers}.')
#         flag = False

# # 인덱스, remove, del, pop() 통해서 마지막 출력에서 [0] 지우기
