# # 딕셔너리
# # 딕셔너리란, 파이싼에서 묶음 데이터를 관리하기 위한 컨테이너 자료형 중 하나이다
# # 키(key): 밸류(value)로 데이터를 관리한다, 이 말은 딕셔너리에는 인덱스가 존재하지 않는다

# members = {
#     '2019-052001': {
#         '이름': '박찬호',
#         '나이': 25,
#         '성별': 'M',
#         '연락처': '010-1234-5678',
#         '이용서비스': ['헬스, 수영'],
#         '할인율': 0
#     },
#     '2019-052004': {
#         '이름': '박용택',
#         '나이': 65,
#         '성별': 'M',
#         '연락처': '010-9012-3456',
#         '이용서비스': '수영',
#         '할인율': 50
#     },
#     '2019-052003': {
#         '이름': '박.세리',
#         '나이': 70,
#         '성별': 'W',
#         '연락처': '010-7890-1234',
#         '이용서비스': '아쿠아로빅',
#         '할인율': 50
#     }
# }

# print(members['2019-052001']['이용서비스'])


# # 함수기본
# # 함수란, 특정 기능을 정의한 구문으로 기능을 재사용하기 위해서 사용한다
# # VS 변수란, 데이터를 관리하기 위한 메모리 공간으로 데이터를 재사용하기 위해 사용한다

# '''
# - 함수 기번
# def 함수이름:
#     기능(실행문)
# '''

# # 인사말이 출력되는 함수를 만들지
# # 함수 정의(선언) --> 함수 선언부
# def printIntro():
#     print('안녕하세요, 좋은 아침인가요?')

# # 함수 호출(call) --> 함수 호출부
# printIntro()


# # 함수는 이렇게 만들자 -> 기능을 최대한 작게, 다른 프로그램에 이식이 간단하도록



# # 계산기 프로그램을 함수를 이용해 만들자

# # (하나의 함수에 많은 기능이 있는 상태)
# def calculator():
#     if operator == 1:
#         print(f'덧셈 결과: {num1 + num2}')

#     elif operator == 2:
#         print(f'뺄셈 결과: {num1 - num2}')

#     elif operator == 3:
#         print(f'곱셈 결과: {num1 * num2}')

#     elif operator == 4:
#         print(f'나눗셈 결과: {num1 / num2}')


# # (하나의 함수에, 하나의 기능만)
# def add():
#     print(f'덧셈 결과: {num1 + num2}')

# def sub():
#     print(f'뺄셈 결과: {num1 - num2}')

# def mul():
#     print(f'곱셈 결과: {num1 * num2}')

# def div():
#     print(f'나눗셈 결과: {num1 / num2}')


# def calculator():
#     if operator == 1:
#         add()

#     elif operator == 2:
#         sub()

#     elif operator == 3:
#         mul()

#     elif operator == 4:
#         div()


# num1 = float(input('1st 숫자 입력: '))
# operator = int(input('연산자 선택: 1.덧셈    2.뺄셈    3.곱셈    4.나눗셈'))
# num2 = float(input('2nd 숫자 입력: '))

# calculator()


# # 유치원에 납품되는 계산기를 만들자 (덧셈, 뺄셈)
# def add():
#     print(f'덧셈 결과: {num1 + num2}')

# def sub():
#     print(f'뺄셈 결과: {num1 - num2}')

# def lowCalculator():
#         if operator == 1:
#             add()

#         elif operator == 2:
#             sub()

    
# num1 = float(input('1st 숫자 입력: '))
# operator = int(input('연산자 선택: 1.덧셈    2.뺄셈    3.곱셈    4.나눗셈'))
# num2 = float(input('2nd 숫자 입력: '))

# lowCalculator()



