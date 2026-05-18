# 컨테이너 자료형
# 여러개의 데이터를 묶어서 관리하는 것을 말함

# # 기존 변수명 선언방식
# fruit1 = '사과'
# fruit2 = '포도'
# fruit3 = '복숭아'

# # 컨테이너 자료형 방식
# fruits = ['사과', '포도', '복숭아']     #컨테이너 자료형: list(리스트)
# print(f'fruits: {fruits}')              #fruits: ['사과', '포도', '복숭아']
# print(f'fruits type: {type(fruits)}')   #fruits type: <class 'list'>

# 파이썬에서 컨테이너 자료형으로는
# 리스트(list), 튜플(tuple), 딕셔너리(dictionery)가 있다

# # 리스트(list) 정의(선언 + 초기화)
# fruits = ['사과', '포도', '복숭아']

# 인덱스(index): 아이템에 부여된 아이템 식별 번호

#    0       1       2
# ['사과', '포도', '복숭아']

# # 아이템 조회
# print(f'fruits[0]: {fruits[0]}')    #fruits[0]: 사과
# print(f'fruits[1]: {fruits[1]}')    #fruits[1]: 포도
# print(f'fruits[2]: {fruits[2]}')    #fruits[2]: 복숭아
# # print(f'fruits[3]: {fruits[3]}')    #IndexError: list index out of range

# # 리스트의 길이(아이템의 개수)
# cnt = len(fruits)
# print(cnt)     #3

# # 리스트의 마지막 아이템의 인덱스 값은 '리스트 길이 -1'이다
# print(f'last data: {fruits[len(fruits)-1]}')    #last data: 복숭아
# print(f'last data: {fruits[0]}')                #last data: 사과

# # 리스트의 전체 데이터 조회
# # 리스트는 반복가능한 객체(데이터)이다 -> 이터러블한 데이터
# for fruits in fruits:
#     print(f'fruits: {fruits}')
# # fruits: 사과
# # fruits: 포도
# # fruits: 복숭아

# for idx, fruits in enumerate(fruits):
#     print(f'index: {idx}, fruits: {fruits}')
# # index: 0, fruits: 사과
# # index: 1, fruits: 포도
# # index: 2, fruits: 복숭아

# # by while문
# i = 0
# fruits = ['사과', '포도', '복숭아']
# while i < len(fruits):
#     print(fruits[1])
#     i += 1
# # 포도
# # 포도
# # 포도

# # 아이템 삽입
# # 리스트 마지막에 삽입
# fruits = ['사과', '포도', '복숭아']
# fruits.append('수박')
# print(f'fruits: {fruits}')
# # fruits: ['사과', '포도', '복숭아', '수박']

# # 특정 위치에 삽입
# fruits.insert(2, '멜론')
# print(f'fruits: {fruits}')
# # fruits: ['사과', '포도', '멜론', '복숭아', '수박']

# # 리스트 연결
# list1 = [1, 2, 3]
# list2 = [11, 12, 13]

# list1.extend(list2)
# print(f'list1: {list1}')            #list1: [1, 2, 3, 11, 12, 13]
# print(f'list2: {list2}')            #list2: [11, 12, 13]

# # 리스트 연결: +
# list3 = list1 + list2       #새로운 메모리 공간에 만들어짐()
# print(f'list3: {list3}')              #list3: [1, 2, 3, 11, 12, 13]

# # 아이템 삭제하기
# sports = ['football', 'baseball', 'volleyball', 'basketball']

# # 마지막 아이템 삭제하기
# sports.pop()
# print(f'sports: {sports}')      #sports: ['football', 'baseball', 'volleyball']

# # 특정 위치 아이템 삭제하기
# sports.pop(1)
# print(f'sports: {sports}')      #sports: ['football', 'volleyball']

# # pop()과 비슷하게 사용할 수 있는 키워드 del
# del sports[1]
# print(f'sports: {sports}')      #sports: ['football']

# # pop() vs del
# nums = [1, 2, 3, 4, 5, 6]
# deletedNum = nums.pop(3)
# print(f'deletedNum: {deletedNum}')     #deletedNum: 4

# # 특정 아이템 삭제 by아이템

# languages = ['c/c++', 'c#', 'java', 'python']
# languages.pop(2)        #['c/c++', 'c#', 'python']

# languages.remove('java')
# print(f'language: {languages}')     #language: ['c/c++', 'c#', 'python']


# # remove()를 이용해서 아이템을 삭제할 때 
# # 삭제하려는 아이템의 개수가 2개 이상일 때 처음 아이템만 삭제된다
# languages = ['c/c++', 'c#', 'java', 'python', 'java']
# languages.remove('java')
# print(f'languages: {languages}')    #languages: ['c/c++', 'c#', 'python', 'java']


# # quiz - 과일 리스트에서 야채를 찾아 삭제하기
# '''
# 다음은 냉장고에 있는 과일을 리스트로 나타낸 것이다
# ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
# 이중 과일이 아닌 '당근'과 '토마토'를 찾아 삭제하는 프로그램
# '''

# fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
# print(f'fruits: {fruits}')   #fruits: ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']

# for item in fruits:
#     if item == '당근' or item == '토마토':
#         fruits.remove(item)
# print(f'fruits: {fruits}')   #fruits: ['사과', '망고', '수박', '포도', '참외']

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

scores = [55, 35, 40, 70, 65, 30]

total           = 0    # 총점
underSubject    = 0    # 과락 과목 개수
average         = 0    # 과목 평균

for score in scores:
    if score < 40:      # 과락 과목 개수
        underSubject += 1

    total += score      # 총합

print(f'40점 미만 과목 수: {underSubject}')     #40점 미만 과목 수: 2
average = total / len(scores)

print(f'평균: {average:.2f}')    #평균: 49.17

# 합격 여부
if underSubject > 0 or average < 60:
    print(f'다음 기회')
else:
    print(f'합격')


