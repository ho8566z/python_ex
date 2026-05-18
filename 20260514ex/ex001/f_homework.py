# # 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
# #  [3, 7, 1, 9, 5]

# # (1)
# numbers = [3, 7, 1, 9, 5]
# numbers.sort()
# print(f'numbers: {numbers}')                        #numbers: [1, 3, 5, 7, 9]
# print(f'numbers: {numbers[len(numbers)-1:]}')       #numbers: [9]

# print(f'numbers: {numbers[-1]}')                    #numbers: 9

# # (2)
# nums = [3, 7, 1, 9, 5]
# maxNum = 0
# for num in nums:
#     if num > maxNum:
#         maxNum = num

# print(f'maxNum: {maxNum}')      #maxNum: 9

# # (3)
# nums = [3, 7, 1, 9, 5]
# print(max(nums))            #9



# # 2. 사용자에게 숫자 입력받아서 1부터 입력한 숫자까지 합계 출력하기

# # (1)
# inputData = []
# userInputData = int(input(f'숫자 입력: '))      #숫자 입력: 10
# print(f'입력한 숫자: {userInputData}')          #입력한 숫자: 10
# inputData.append(userInputData + 1)

# sum = inputData[len(inputData)-1]
# cnt = 0

# for plus in range(1, sum):
#     cnt += plus
# print(f'1부터 입력한 숫자까지의 합: ', cnt)       #1부터 입력한 숫자까지의 합:  55

# # (2)
# userInputNum = int(input('양수입력: '))
# total = 0
# for num in range(1, userInputNum+1):
#     total += num
# print(f'total: {total}')
# # 양수입력: 10
# # total: 55



# # 3. 리스트에 있는 숫자 중 짝수만 출력하기
# # [1,2,3,4,5,6]
# numbers = [1,2,3,4,5,6]

# for num in numbers:
#     if num % 2 == 0:
#         print(f'numbers의 짝수는: {num}')
# # numbers의 짝수는: 2
# # numbers의 짝수는: 4
# # numbers의 짝수는: 6



# # 4. 리스트 숫자를 오름차순 정렬하기
# # [5,1,7,3]
# numbers = [5,1,7,3]
# numbers.sort()
# print(f'numbers: {numbers}')        #numbers: [1, 3, 5, 7]



# # 5. 리스트 숫자를 내림차순 정렬하기
# # [5,1,7,3]
# numbers = [5,1,7,3]
# numbers.sort(reverse=True)
# print(f'numbers: {numbers}')        #numbers: [7, 5, 3, 1]



# # 6. 리스트 안 숫자의 평균 구하기 
# # [10,20,30]
# numbers = [10,20,30]
# total = 0
# average = 0

# for number in numbers:
#     total += number
    
# average = total / len(numbers)

# print(f'total: {total}')                   #total: 60
# print(f'numbers의 평균: {average}')         #numbers의 평균: 20.0



# # 7. 리스트에서 가장 작은 숫자 찾기
# # (min() 사용 금지)

# # (1)
# numbers = [3, 55, 16, 1, 12, 63]
# numbers.sort()
# print(f'numbers에서 가장 작은 숫자: {numbers[0]}')    #numbers에서 가장 작은 숫자: 1

# # (2)
# nums = [3, 55, 16, 1, 12, 63]
# minNum = nums[0]
# for num in nums:
#     if num < minNum:
#         minNum = num
# print(f'minNum: {minNum}')      #minNum: 1



# # 8. 1부터 100까지 숫자 중 3의 배수와 5의 배수 출력하기

# # (1, 공배수 버전)
# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(f'3과 5의 공배수: {num}')
# # 3과 5의 공배수: 15
# # 3과 5의 공배수: 30
# # 3과 5의 공배수: 45
# # 3과 5의 공배수: 60
# # 3과 5의 공배수: 75
# # 3과 5의 공배수: 90

# # (2, 3의 배수와 5의 배수 따로)
# for num in range(1, 101):
#     if num % 3 == 0:
#         print(f'{num}은 3의 배수')

#     if num % 5 == 0:
#         print(f'{num}은 5의 배수')
# 3은 3의 배수
# # 5은 5의 배수
# # 6은 3의 배수
# # 9은 3의 배수
# # 10은 5의 배수
# # 12은 3의 배수
# # 15은 3의 배수
# # 15은 5의 배수
# # 18은 3의 배수
# # 20은 5의 배수
# # 21은 3의 배수
# # 24은 3의 배수
# # 25은 5의 배수
# # 27은 3의 배수
# # 30은 3의 배수
# # 30은 5의 배수
# # 33은 3의 배수
# # 35은 5의 배수
# # 36은 3의 배수
# # 39은 3의 배수
# # 40은 5의 배수
# # 42은 3의 배수
# # 45은 3의 배수
# # 45은 5의 배수
# # 48은 3의 배수
# # 50은 5의 배수
# # 51은 3의 배수
# # 54은 3의 배수
# # 55은 5의 배수
# # 57은 3의 배수
# # 60은 3의 배수
# # 60은 5의 배수
# # 63은 3의 배수
# # 65은 5의 배수
# # 66은 3의 배수
# # 69은 3의 배수
# # 70은 5의 배수
# # 72은 3의 배수
# # 75은 3의 배수
# # 75은 5의 배수
# # 78은 3의 배수
# # 80은 5의 배수
# # 81은 3의 배수
# # 84은 3의 배수
# # 85은 5의 배수
# # 87은 3의 배수
# # 90은 3의 배수
# # 90은 5의 배수
# # 93은 3의 배수
# # 95은 5의 배수
# # 96은 3의 배수
# # 99은 3의 배수
# # 100은 5의 배수



# # 9. 사용자가 입력한 숫자를 리스트에 저장하다가 0을 입력하면 종료 후 리스트 출력하기
# # [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]

# # (1)
# numbers = []
# flag = True

# while flag:

#     userNum = int(input(f'숫자를 입력하세요. '))
#     numbers.append(userNum)
#     print(f'입력한 숫자는? {userNum}')
#     if userNum == 0:
#         print(f'0을 입력해 종료합니다. ')
#         print(f'입력한 숫자 목록: {numbers}')
#         flag = False



# # (2)
# nums = []

# while True:
#     userInputNumber = int(input('정수입력: '))

#     if userInputNumber == 0:
#         break

#     nums.append(userInputNumber)

# print(f'nums: {nums}')


