# # split(쪼갠다)
# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
# print(f'names: {names}')
# print(f'names type: {type(names)}')
# # names: ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
# # names type: <class 'tuple'>


# str = "박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아"
# splitedStr = str.split(" ")     #spit()으로 나눌 때는 ' '나 =, + 등으로 나눌 수 있다
# print(f'splitedStr: {splitedStr}')
# print(f'splitedStr type: {type(splitedStr)}')
# # splitedStr: ['박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아']
# # splitedStr type: <class 'list'>

# # list -> tuple: split으로 list가 된 것을 다시 tuple로 변형할 때
# tuple(splitedStr)
# print(f'splitedStr: {splitedStr}')
# print(f'splitedStr type: {type(splitedStr)}')
# # splitedStr: ['박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아']
# # splitedStr type: <class 'list'>


# 튜플 안의 아이템 유/무 확인하기
# in과 not in을 사용하면 튜플 안에 특정 아이템의 존재 유/무를 확인할 수 있다

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'colors Green: {'Green' in colors}')         #colors Green: True
# print(f'colors Green++: {'Green++' in colors}')     #colors Green++: False

# if 'Green' in colors:
#     print('colors에는 Green이 있다.')
# else:
#     print('colors에는 Green이 없다.')
# #colors에는 Green이 있다.

# if 'Green' not in colors:
#     print('colors에는 Green이 없다.')
# else:
#     print('colors에는 Green이 있다.')
# #colors에는 Green이 있다.


# # quiz - 학사경고 프로그램 만들기
# '''
# scores는 1학기 성적을 튜플로 나타낸 것이다. F학점이 있으먄 '경고'를 출력하는 프로그램
# scores = ('A', 'A+', 'B', 'B-', 'F')
# '''

# scores = ('A', 'A+', 'B', 'B-', 'F')
# if 'F' in scores:
#     print(f'경고')
# else:
#     print(f'경고 없음')
# #경고

# scores = ('A', 'A+', 'F', 'B', 'B-', 'F')
# fCnt = scores.count('F')
# print(f'F학점 개수: {fCnt}')        #F학점 개수: 2



# # 튜플 결합
# # at list
# nums1 = [1, 2, 3]
# nums2 = [11, 12, 13]

# # 1st
# nums1.extend(nums2)
# print(f'nums1: {nums1}')        #nums1: [1, 2, 3, 11, 12, 13]
# print(f'nums2: {nums2}')        #nums2: [11, 12, 13]

# # 2nd
# result = nums1 + nums2
# print(f'nums1: {nums1}')        #nums1: [1, 2, 3]
# print(f'nums2: {nums2}')        #nums2: [11, 12, 13]
# print(f'result: {result}')      #result: [1, 2, 3, 11, 12, 13]


# # at tuple
# nums1 = (1, 2, 3)
# nums2 = (11, 12, 13)

# # nums1.extend(nums2)
# # #Exception has occurred: AttributeError 
# # :속성 에러(튜플은 수정이 불가능 하기 때문에 num1이라는 tuple의 데이터 수정하는 것, 또한 불가능)
# # print(f'nums1: {nums1}')
# # print(f'nums2: {nums2}')

# result = nums1 + nums2
# print(f'result: {result}')      #result: (1, 2, 3, 11, 12, 13)



# num1 = 10
# num2 = num1
# print(f'num1: {num1}')      #num1: 10
# print(f'num2: {num2}')      #num2: 10

# num1 = 100
# print(f'num1_1: {num1}')    #num1_1: 100
# print(f'num2_2: {num2}')    #num2_2: 10

# #-------------------------------------------------------------#
# #-------------------------------------------------------------#

# # 얕은 복사
# nums1 = [1, 2, 3]
# nums2 = nums1
# print(f'nums1: {nums1}')        #nums1: [1, 2, 3]
# print(f'nums2: {nums2}')        #nums2: [1, 2, 3]

# nums1[0] = 100
# print(f'nums1_1: {nums1}')      #nums1_1: [100, 2, 3]
# print(f'nums2_2: {nums2}')      #nums2_2: [100, 2, 3]

# #-------------------------------------------------------------#

# # 깊은 복사
# nums1 = [1, 2, 3]
# nums2 = [0, 0, 0]

# for idx, num in enumerate(nums1):
#     nums2[idx] = num

# print(f'nums1: {nums1}')        #nums1: [1, 2, 3]
# print(f'nums2: {nums2}')        #nums2: [1, 2, 3]
# # (얕은 복사와 달리, 출력된 값이 같더라도 각각 인식한 데이터는 다른 출처를 가지고 있음)

# #-------------------------------------------------------------#

# # copy (=깊은 복사 / 데이터 연산 속도가 훨씬 빠름)

# import copy

# numA = [1, 2, 3, 4, 5]
# numB = copy.deepcopy(numA)

# numB[0] = 100

# print(f'numA: {numA}')      #numA: [1, 2, 3, 4, 5]
# print(f'numB: {numB}')      #numB: [100, 2, 3, 4, 5]

# #-------------------------------------------------------------#

# # copy_2 (사용량 저조한 버전)
# import copy

# numA = [1, 2, 3, 4, 5]
# numB = numA.copy()

# numB[0] = 100

# print(f'numA: {numA}')      #numA: [1, 2, 3, 4, 5]
# print(f'numB: {numB}')      #numB: [100, 2, 3, 4, 5]



# # 튜플 슬라이싱: tuple slicing
# animals = ('호랑이', '사자', '곰', '여우', '늑대')
# print(f'animals: {animals}')    #animals: ('호랑이', '사자', '곰', '여우', '늑대')

# print(f'animals[:3]: {animals[:3]}')        #animals[:3]: ('호랑이', '사자', '곰')
# print(f'animals[1:4]: {animals[1:4]}')      #animals[1:4]: ('사자', '곰', '여우')
# print(f'animals[:-2]: {animals[:-2]}')      #animals[:-2]: ('호랑이', '사자', '곰')
# print(f'animals[-1:-2]: {animals[-1:-2]}')  #animals[-1:-2]: ()
# print(f'animals[-3:-1]: {animals[-3:-1]}')  #animals[-3:-1]: ('곰', '여우')



# # quiz - 슬라이싱 연습하기
# '''
# fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
#  - 인덱스 2부터 4까지의 아이템을 출력하시오.
#  - 인덱스 0부터 3까지의 아이템을 출력하시오.
#  - 인덱스 3부터 끝까지의 아이템을 출력하시오.
# '''

# fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
# print(f'fruits[2:5]: {fruits[2:5]}')    #fruits[2:5]: ('plum', 'watermelon', 'peach')
# print(f'fruits[2:]: {fruits[2:]}')      #fruits[2:]: ('plum', 'watermelon', 'peach')

# print(f'fruits[0:4]: {fruits[0:4]}')    
# #fruits[0:4]: ('apple', 'banana', 'plum', 'watermelon')

# print(f'fruits[3:]: {fruits[3:]}')      
# #fruits[3:]: ('watermelon', 'peach')


# # 리스트와 튜플 간 변환(형변화, casting)
# '''
# 불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 한다
# 또한 리스트로 선언된 데이터를 수정이 안 되도록 하려면 변환해야 한다
# 다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있다
# '''

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# # Orange => 오렌지
# # colors[1] => 오렌지
# colors = list(colors)
# print(f'colors type: {type(colors)}')   #colors type: <class 'list'>

# colors[1] = '오렌지'
# print(f'colors: {colors}')
# #colors: ['Red', '오렌지', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']

# colors = tuple(colors)
# print(f'colors: {colors}')
# #colors: ('Red', '오렌지', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'colors type: {type(colors)}')   #colors type: <class 'tuple'>



# # quiz - 튜플 정렬하기
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# colors = list(colors)
# # print(f'colors: {colors}')
# # print(f'colors type: {type(colors)}')
# colors.sort()
# print(f'colors: {colors}')
# print(f'colors type: {type(colors)}')
# # colors: ['Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow']
# # colors type: <class 'list'>

# colors = tuple(colors)
# print(f'colors: {colors}')
# print(f'colors type: {type(colors)}')
# # colors: ('Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow')
# # # colors type: <class 'tuple'>

# #-------------------------------------------------------------#

# # re 정렬
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')

# reColors = sorted(colors)
# print(f'reColors: {reColors}')
# print(f'reColors type: {type(reColors)}')
# # reColors: ['Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow']
# # reColors type: <class 'list'>

# reColors = tuple(sorted(colors))
# print(f'reColors: {reColors}')
# print(f'reColors type: {type(reColors)}')
# # reColors: ('Blue', 'Green', 'Indigo', 'Orange', 'Purple', 'Red', 'Yellow')
# # reColors type: <class 'tuple'>

