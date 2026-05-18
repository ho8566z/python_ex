# # CRUD
# '''
# C: Create   생성, 추가
# R: Read     조회
# U: Update   수정
# D: Delete   삭제
# '''

# '''
# 딕셔너리(Dictionary): {key: value}
# '''

# student = {
#     '학번': 20260518,
#     '이름': '홍길동',
#     '나이': 20,
#     '성별': 'M',
#     '연락처': '010-0001-0002'
# }

# print(f'student: {student}')
# print(f'studrnt type: {type(student)}')
# # student: {'학번': 20260518, '이름': '홍길동', '나이': 20, '성별': 'M', '연락처': '010-0001-0002'}
# # studrnt type: <class 'dict'>

# sNo = student['학번']
# print(f'sNo: {sNo}')
# print(f'sNo type: {type(sNo)}')
# # sNo: 20260518
# # sNo type: <class 'int'>

# sName = student['이름']
# print(f'sName: {sName}')            #sName: 홍길동

# sName = student['이름'] = '홍길순'
# print(f'sName: {sName}')            #sName: 홍길순

# del student['연락처']
# print(f'student: {student}')
# #student: {'학번': 20260518, '이름': '홍길순', '나이': 20, '성별': 'M'}

# # keys(), values(), items()
# # keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다. 뽑은 키들은 리스트와 비스한 데이터 타입이다
# keys = student.keys()
# print(f'keys: {keys}')
# print(f'keys type: {type(keys)}')
# # keys: dict_keys(['학번', '이름', '나이', '성별'])
# # keys type: <class 'dict_keys'>

# for key in keys:
#     print(f'key: value = {key}: {student[key]}')
# # key: value = 학번: 20260518
# # key: value = 이름: 홍길순
# # key: value = 나이: 20
# # key: value = 성별: M

# #values(): 딕셔너리에서 밸류값들만 몽띵 뽑는다. 뽑은 밸류들은 리스트와 비슷한 데이터 타입이다
# values = student.values()
# print(f'values: {values}')
# print(f'values type: {type(values)}')
# # values: dict_values([20260518, '홍길순', 20, 'M'])
# # values type: <class 'dict_values'>

# for value in values:
#     print(f'value: {value}')
# # value: 20260518
# # value: 홍길순
# # value: 20
# # value: M

# items = student.items()         #key & value
# print(f'items: {items}')
# # items: dict_items([('학번', 20260518), ('이름', '홍길순'), ('나이', 20), ('성별', 'M')])
# for item in items:
#     print(f'item: {item}')
#     print(f'item[0], item[1]: {item[0]}, {item[1]}')
# # item: ('학번', 20260518)
# # item[0], item[1]: 학번, 20260518
# # item: ('이름', '홍길순')
# # item[0], item[1]: 이름, 홍길순
# # item: ('나이', 20)
# # item[0], item[1]: 나이, 20
# # item: ('성별', 'M')
# # item[0], item[1]: 성별, M

# # (딕셔너리 내부의 키값과 밸류값은 튜플로 구성되어 있다)

# for key, value in items:
#     print(f'key, value: {key}: {value}')
# # key, value: 학번: 20260518
# # key, value: 이름: 홍길순
# # key, value: 나이: 20
# # key, value: 성별: M

# '''
# key, value = ('학번', 00010002)
# '''

# # 구조분해할당
# # a, b = (10, 20)
# # print(f'a: {a}, b: {b}')

# c = (10, 20)
# a = c[0]
# b = c[1]
# print(f'a: {a}, b: {b}')        #a: 10, b: 20

# a = 10
# b = 20

# # swapping ==> a: 20, b= 10
# temp = a
# a = b       #a: 20
# b = temp    #b: 10

# a, b = b, a
# print(f'a: {a}, b: {b}')        #a: 20, b: 10

# scores = [10, 20, 30, 40, 50, 60]
# '''
# a = 10
# b = 20
# c = [30, 40, 50, 60]
# '''

# a, b, *c = scores
# print(f'a: {a}')        #a: 10
# print(f'b: {b}')        #b: 20
# print(f'c: {c}')        #c: [30, 40, 50, 60]



# # quiz - 다음은 스포츠센터 회원정보를 나타낸 표이다
# # 표를 보고 파이썬을 이용해서 컨테이너 자료형으로 만들자

# members = {
#     '2019-052001': '박찬호+25+M+010-0001-0002+헬스,수영+0'
# }

# info = members['2019-052001']
# print(f'info: {info}')      #info: 박찬호+25+M+010-0001-0002+헬스,수영+0
# infos = info.split('+')
# print(f'infos: {infos}')    #infos: ['박찬호', '25', 'M', '010-0001-0002', '헬스,수영', '0']

# members = {
#     '2019-052001': {
#         '이름': '박찬호',
#         '나이': 25,
#         '성별': 'M',
#         '연락처': '010-0001-0002',
#         '이용서비스': ['헬스', '수영'],
#         '할인율': 0
#     }
# }

# print(members['2019-052001'])
# #{'이름': '박찬호', '나이': 25, '성별': 'M', '연락처': '010-0001-0002', 
# # '이용서비스': '헬스,수영', '할인율': '0'}
# print(members['2019-052001']['이름'])           #박찬호
# print(members['2019-052001']['나이'])           #25
# print(members['2019-052001']['연락처'])         #010-0001-0002
# print(members['2019-052001']['이용서비스'])      #['헬스', '수영']
# print(members['2019-052001']['할인율'])         #0

