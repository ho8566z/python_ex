# 컨테이나 자료형(container data type)

# 많은 데이터를 효율적으로 관리하기 위해 사용한다
# list(리스트)
# tuple(튜플)
# dictionary(딕셔너리)

# 기초 데이터 타입: 변수명 선언과 초기화에 따른 데이터 입력/삽입
# 참조 데이터 타입(레퍼런스 데이터 타입): 리스트명의 데이터는 []내부의 첫번째 데이터의 메모리 
# 주소를 담고 있다 때문에 데이터를 직접 관리하지 않고, '참조'한다


# 딕셔너리(dictionary)
'''
딕셔너리는 리스트, 튜플과 같이 파이썬에서 많이 사용되는 컨테이너 자료형이다
리스트가 인덱스를 이용해 아이템을 참조한다면, 딕셔너리는 인덱스 대신에 '키(key)'를 
이용해 아이템을 참조한다

딕셔너리는 '키(key)'와 '값(value)'로 이루어져 있고, 이를 '키 값'이라고 한다
= '키-> 키값 : k' / '값-> 밸류값 : v'
'''

# 딕셔너리 정의
# 딕셔너리 -> {}

# sportsPlayers = {}
# ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43}
# # {'박찬호': 48, '박지성': 40}: 앞의 이름은 '키', 뒤의 나이는 '값'
# # 딕셔너리를 선언할 때는 '중 괄호' 사용, 키값의 구분은 ','로서 구분한다

# # ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43, '박지성': 100}
# #-> '키(key)'값은 절대로 중복되어서는 안된다

# # ages = {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43, '지성팍': 40}
# #-> '밸류(value)'값은 중복되어도 상관없다

# print(f'ages: {ages}')
# #ages: {'박찬호': 48, '박지성': 40, '박세리': 50, '이승엽': 43}
# print(f'ages type: {type(ages)}')       #ages type: <class 'dict'>



# # dictionary - ex)

# scores = {
#     'c/c++': 'A',
#     'Java': 'B+',
#     '네트워킹': 'C',
#     '보안': 'A+',
#     '해킹': 'F',
#     '시스템': 'C+'
# }

# print(f'scoresL {scores}')
# #scoresL {'c/c++': 'A', 'Java': 'B+', '네트워킹': 'C', '보안': 'A+', 
# # '해킹': 'F', '시스템': 'C+'}



# # 마지막 내용
# # 리스트, 튜플, 딕셔너리

# listVar1 = [1, 3.14, 'hello']
# print(f'listVar1: {listVar1}')
# print(f'listVar1 type: {type(listVar1)}')
# # listVar1: [1, 3.14, 'hello']
# # listVar1 type: <class 'list'>

# listVar2 = (1, 3.14, 'hello')
# print(f'listVar2: {listVar2}')
# print(f'listVar2 type: {type(listVar2)}')
# # listVar2: (1, 3.14, 'hello')
# # listVar2 type: <class 'tuple'>

# listVar3 = {
#     'AAA': 10,
#     'BBB': 3.14,
#     'CCC': '안녕하세요'
# }
# print(f'listVar3: {listVar3}')
# print(f'listVar3 type: {type(listVar3)}')
# # listVar3: {'AAA': 10, 'BBB': 3.14, 'CCC': '안녕하세요'}
# # listVar3 type: <class 'dict'>


# listVar10 = [1, 2, 3]
# print(f'listVar10: {listVar10}')
# #listVar10: [1, 2, 3]

# listVar20 = [10, 20, 30, listVar10]
# print(f'listVar20: {listVar20}')
# #listVar20: [10, 20, 30, [1, 2, 3]]

# print(f'listVar20[3]: {listVar20[3]}')
# #listVar20[3]: [1, 2, 3]

# # 2차원 배열
# print(f'listVar20[3][1]: {listVar20[3][1]}')
# #listVar20[3][1]: 2


# print(type(listVar20[2]))       #<class 'int'>
# print(type(listVar20[3]))       #<class 'list'>



# dicts = {
#     'name': '박찬호',
#     'age': 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구']
# }

# print(f'dicts: {dicts}')
# # dicts: {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 
# # 'hobby': ['축구', '농구', '배구']}

# print(dicts['hobby'])       #['축구', '농구', '배구']
# print(dicts['hobby'][1])    #농구


# '''
# 1차원: nums[]
# 2차원: nums[][]
# 3차원: nums[][][]
# 4차원: nums[][][][]
# N차원: nums[][][][] --- []
# -데이터 구조 설계의 권장 차원: 2차원 까지만
# '''



# dicts = {
#     'name': '박찬호',
#     'age': 20,
#     'addr': '대전 중구',
#     'hobby': ['축구', '농구', '배구'],
#     (1, 2, 10): 100
# }

# print(f'dicts: {dicts}')
# # dicts: {'name': '박찬호', 'age': 20, 'addr': '대전 중구', 
# # 'hobby': ['축구', '농구', '배구'], (1, 2, 10): 100}
# #(튜플 또한 '키'값으로 '밸류'값을 담을 수 있다 -> 튜플의 아이템은 변화하지 않기 때문에)
# #(but, 리스트는 튜플과 달리 '키'값으로 '밸류'값을 담을 수 없다 
# # -> 리스트의 아이템을 변화시킬 수 있기 때문에)




#---------------------------------------------------------------------##

# 딕셔너리 조회/삽입/수정/삭제

'''
딕셔너리 '조회/삽입/수정/삭제'를 CRUD라고 한다
CRUD라는 용어는 개발자라면 반드시 알고 있어야 한다
CRUD는 Create, Read, Update, Delete를 말한다
즉, 데이터를 생성(Create), 조회(Read), 수정(Update), 삭제(Delete) 하는 것을 말한다
그렇다면, 딕셔너리에서 CRUD는 딕셔너리 컨테이너 자료형에 
데이터를 추가(Create), 조회(Read), 수정(Update), 삭제(Delete) 하는 것을 말한다
CRUD는 프로그래밍 뿐만 아니라 데이터베이스에서도 사용되는 용어이다
'''

# # 생성 및 추가(Create)
# dicContainer = {
#     '이름': '홍길동',
#     '나리': 25,
#     '주소': '대전 중구',
#     '취미': ['축구', '수영', '조깅'],
#     '몸무게': 87.5
# }
# print(f'dicContainer: {dicContainer}')
# # dicContainer: {'이름': '홍길동', '나리': 25, '주소': '대전 중구', 
# # '취미': ['축구', '수영', '조깅'], '몸무게': 87.5}


# # ex) dicContainer[키(값)] = 밸류(값)
# dicContainer['연락처'] = '010-0001-0002'
# print(f'dicContainer: {dicContainer}')
# # dicContainer: {'이름': '홍길동', '나리': 25, '주소': '대전 중구', 
# # '취미': ['축구', '수영', '조깅'], '몸무게': 87.5, '연락처': '010-0001-0002'}


# # 조회(Read)
# print(f'이름: {dicContainer['이름']}')
# # 이름: 홍길동


# # 수정(Update)
# dicContainer['몸무게'] = 55
# print(f'몸무게: {dicContainer['몸무게']}')
# # 몸무게: 55


# # 삭제(Delete)
# del dicContainer['몸무게']
# print(f'dicContainer: {dicContainer}')
# # dicContainer: {'이름': '홍길동', '나리': 25, '주소': '대전 중구', 
# # '취미': ['축구', '수영', '조깅'], '연락처': '010-0001-0002'}


# # 부가 기능
# # 1. 아이템 개수 조회
# print(f'아이템 개수 조회: {len(dicContainer)}')
# # 아이템 개수 조회: 5

# # 2. 전체키 & 밸류 조회
# # 2-1 전체키
# disKeys = dicContainer.keys()
# print(f'disKeys: {disKeys}')
# # disKeys: dict_keys(['이름', '나리', '주소', '취미', '연락처'])

# for key in disKeys:
#     print(f'{key} : {dicContainer[key]}')

# # 2-2 밸류
# dicValues = dicContainer.values()
# print(f'dicValues: {dicValues}')
# # dicValues: dict_values(['홍길동', 25, '대전 중구', 
# # ['축구', '수영', '조깅'], '010-0001-0002'])


# # 3. 키와 밸류를 한방에 조회
# for key, value in dicContainer.items():
#     print(f'{key}: {value}')
# # 이름: 홍길동
# # 나리: 25
# # 주소: 대전 중구
# # 취미: ['축구', '수영', '조깅']
# # 연락처: 010-0001-0002


# print(dicContainer.items())
# # dict_items([('이름', '홍길동'), ('나리', 25), ('주소', '대전 중구'), 
# # ('취미', ['축구', '수영', '조깅']), ('연락처', '010-0001-0002')])
# print(type(dicContainer.items()))
# # <class 'dict_items'>



# # quiz - 중간고사 성적 관리 프로그램 만들기
# '''
# 아래 시나리오를 기반으로 딕셔너리를 이용해서 중간고사 성적 관리 프로그램을 만들자
# -1 중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+, 해킹은 F, 시스템은 C+)을 
# 저장하는 딕셔너리를 만든다
# -2 'java'와 같은 '시스템'과목의 성적을 조회한다
# -3 추가로 2과목의 성적(파이썬은 AOS는 A+)을 삽입한다
# -4 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다
# -5 전체과목과 성적을 조회하여 최종 성적표를 출력한다
# '''

# scores = {
#     'C/C++': 'A',
#     'Java': 'B+',
#     '모바일': 'C',
#     '보안': 'A+',
#     '해킹': 'F',
#     '시스템': 'C+'
# }

# print(f'Java: {scores['Java']}')          #java: B+
# print(f'시스템: {scores['시스템']}')        #시스템: C+

# scores['파이썬'] = 'A'
# scores['OS'] = 'A+'
# print(f'scores: {scores}')
# # scores: {'C/C++': 'A', 'Java': 'B+', '모바일': 'C', '보안': 'A+', 
# # '해킹': 'F', '시스템': 'C+', '파이썬': 'A', 'OS': 'A+'}

# scores['Java'] = 'F'
# scores['시스템'] = 'A'
# print(f'scores: {scores}')
# # # scores: {'C/C++': 'A', 'Java': 'F', '모바일': 'C', '보안': 'A+', 
# # # '해킹': 'F', '시스템': 'A', '파이썬': 'A', 'OS': 'A+'}

# for key in scores.keys():
#     print(f'{key}:\t {scores[key]}')
# # C/C++:   A : 4.5
# # Java:    F : 0
# # 모바일:  C : 2.0
# # 보안:    A+ : 4.5
# # 해킹:    F : 0
# # 시스템:  A : 4.0
# # 파이썬:  A : 4.0
# # OS:      A+ : 4.5

# '''
# A+ : 4.5
# A0 : 4.0
# B+ : 3.5
# B0 : 3.0
# C+ : 2.5
# C0 : 2.0
# F0 : 0
# '''

# creditScores = {
#     'A+' : 4.5,
#     'A' : 4.0,
#     'B+' : 3.5,
#     'B' : 3.0,
#     'C+' : 2.5,
#     'C' : 2.0,
#     'F' : 0
# }

# totalScore = 0
# averageScore = 0

# for key in scores.keys():
#     totalScore += creditScores[scores[key]]
#     print(f'{key}:\t{scores[key]}')
# # C/C++:  A
# # Java:   F
# # 모바일: C
# # 보안:   A+
# # 해킹:   F
# # 시스템: A
# # 파이썬: A
# # OS:     A+

# print(f'totalScore: {totalScore}')              #totalScore: 23.0
# averageScore = totalScore / len(scores)
# print(f'averageScore: {averageScore}')          #averageScore: 2.875


