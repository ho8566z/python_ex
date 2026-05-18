# 함수(function)

# python에서는 '함수'가 핵심
# java에서는 '클래스'가 핵심

# 함수란, 특정 수식에 x값을 대입하면 y값이 정해지는 것으로 "y=f(x)" 라고 한다
# 함수의 구조: y = 3x + 5의 수식에 x값을 '2'을 대입하면, y값은 '11'로 정해진다

# 프로그래밍의 함수 또한 수학의 함수와 동일하게 값을 넣어주면 특정 기능을 수행한 연산 결과를
# 출력한다. 여기서 특정 기능이란 덧셈 같은 비교적 간단한 연산부터 네트워크 연결, 회원 인증,
# 메일 발송과 같이 복잡하고 어려운 작업까지 모두 포함한다.

# 복잡한 함수 ex)
# 네트워크 주소 => 네트워크 연결 가능 => 연결 결과
# 아이디, 패스워드 => 회원 인증 가능 => 인증 결과

# 함수 종류
# 1. 내장 함수: 파이썬에서 기본적으로 제공하는 함수         ex) print(), input() 등
# 2. 사용자 함수: 사용자가 자신의 입장의 맞게 만드는 함수


# 코드(기능) 재사용 -> 함수
# 데이터 재사용 -> 변수

# 모듈화
# 모듈은 특정 기능의 작은 프로그램을 뜻한다. 함수를 사용한다는 것은 특정 기능을 모듈화한다는 
# 것으로, 특정 기능이 함수로 모듈화되면 다른 프로그램에 쉽게 이식하여 사용할 수 있고, 시간도 단축됨


# # 함수 정의하기
# '''
# 사용자 함수를 만든다는 것을 '함수를 정의한다' 라고 한다.
# 함수를 정의할 때, 'def' 키워드를 사용한다. 그리고 함수명 콜론(:), 실행부를 이용한다.
# '''

# '''
# num = 10                        <=변수 선언
# def 함수명():                    <=함수 선언
#     실행부(함수 기능)
# '''

# def greet():
#     print('안녕하세요.')
#     print('반갑습니다.')
#     print('저는 홍길동입니다.')

# '''
# 함수명 규칙
# 1. 내장 함수명과 동일하면 안된다.
# 2. 첫 글자는 주로 소문자를 사용하자.
# 3. 첫 글자는 숫자로 시작할 수 없다.     ex) 1greet(): x, greet1(): o
# 4. 특수문자를 사용할 경우에는 _(언더바)만 사용하자.
#     (그 이외의 특수문자는 사용금지)
# 5. 2개 이상의 단어가 조합되는 경우, 스네이크 또는 카멜 표기법을 사용하자.
#     (스네이크: send_message():, 카멜: sendMessage():)
# '''

# # quiz - 온도센서 작동 시스템 만들기
# # 온도센서 작동을 시작하고 멈추는 함수를 정의하자
# # 함수명은 힘수의 기능을 이해하기 쉽게 작명하자

# # 함수 정의부/선언부
# def startTemperatureSensor():
#     print('온도센서 작동을 시작합니다.')

# def stopTemperatureSensor():
#     print('온도센서 작동을 중지합니다.')

# # 함수 호출부
# startTemperatureSensor()        # 온도센서 작동을 시작합니다.
# stopTemperatureSensor()         # 온도센서 작동을 중지합니다.



# # quiz - 내 노트북은 몇 인치일까?
# '''
# 고등학교 졸업 기념으로 노트북을 하나 장만했다.
# 노트북 사이즈에 맞는 파우치를 하나 구매하려는데, 사이즈 표에는 인치로만
# 표기되어 있다
# cm를 인치로 바꿔주는 함수를 만들자
# (1inch = 0.393701cm)
# '''

# def convertUnit():
#     lengthCM = float(input(f'길이(cm) 입력: '))
#     print(f'{lengthCM * 0.393701}inch')

# convertUnit()
# # 길이(cm) 입력: 10
# # 3.9370100000000003inch

# convertUnit()
# convertUnit()
# # 길이(cm) 입력: 20
# # 7.874020000000001inch
# # 길이(cm) 입력: 30
# # 11.81103inch

# # 함수를 여러번 선언하면, 선언한 만큼 실행된다.
# # 함수를 선언하고, 사용하지 않으면 메모리만 차지해 메모리가 낭비된다



# # quiz - 이동 거리를 계산하는 함수
# '''
# 길동이는 5시간 동안 3km의 속도로 등산을 했다.
# 길동이가 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는 프로그램을
# 함수를 이용해 만들자
# '''

# def calculateDistance():
#     print(f'이동거리: {hourData * speedData}')

# hourData = float(input('이동 시간: '))
# speedData = float(input('이동 속도: '))

# calculateDistance()
# # 이동 시간: 5
# # 이동 속도: 3
# # 이동거리: 15.0


# # 파이썬에서만, 함수 안에서나 바깥에서 변수를 선언하거나 데아터를 입력받아도 
# # 함수 실행에 있어서 문제가 발생하지 않음.


# # pass 키워드
# def calculateNumber():
#     pass        # 실행구문이 없어서 error가 뜨기 때문에 이를 방지하기 위해


# # 함수 내에서 또 다른 함수 호출
# # 함수 안에서 또 다른 함수를 호출하는 것

# def fun1():
#     print('fun1() called')

# def fun2():
#     print('fun2() called')

# def fun3():
#     fun1()
#     fun2()
#     print('fun3() called')


# fun1()          #fun1() called

# fun2()          #fun2() called

# fun3()          #fun1() called
#                 #fun2() called
#                 #fun3() called


# # 재귀 함수

# def fun4():
#     print('fun4() called')
#     fun4()

# fun4()
# # fun4() called
# # fun4() called
# # -----------------------
# # fun4() called
# # Traceback (most recent call last):
# #   File "c:\lyh\python\python_ex\20260518ex\ex001\function01.py", line 160, in <module>
# #     fun4()
# #     ~~~~^^
# #   File "c:\lyh\python\python_ex\20260518ex\ex001\function01.py", line 158, in fun4
# #     fun4()
# #     ~~~~^^
# #   File "c:\lyh\python\python_ex\20260518ex\ex001\function01.py", line 158, in fun4
# #     fun4()
# #     ~~~~^^
# #   File "c:\lyh\python\python_ex\20260518ex\ex001\function01.py", line 158, in fun4
# #     fun4()
# #     ~~~~^^
# #   [Previous line repeated 996 more times]
# # RecursionError: maximum recursion depth exceeded

# # (함수는 변수와 달리, 메모리 상에서 무한 복사 및 복제가 되면서 매모리가 full되면서 셧다운되기 
# # 전에 시스템이 중단한다: '[Previous line repeated 996 more times]' 
# # 996번 이상 실행 불가하다는 것)

# # (fun4을 실행할 때, 1번 실행하고 안에 있는 fun4 함수를 다시 불러와서 메모리의 다른 곳에 
# # 다시 fun4를 가리키는 호출부를 만들고 이게 계속되는 상태이다)



# # quiz - 다국어 인사말 프로그램을 함수를 이용해 만들자
# '''
# 사용자가 출신 국가를 선택하면, 해당 국가의 인사말이 출력되는 프로그램을
# 함수를 이용해 만들자
# 1.한국     2.USA     3.Japan
# '''

# def introKor():
#     print('안녕')

# def introUsa():
#     print('Hello')

# def introJap():
#     print('おはよう')


# selectedMenuNum = int(input('Where are you from? - 1.한국    2.USA    3.Japan'))

# if  selectedMenuNum == 1:
#     introKor()                  #안녕

# elif selectedMenuNum == 2:
#     introUsa()                  #Hello

# elif selectedMenuNum == 3:
#     introJap()                  #おはよう



# # quiz - 계산기 프로그램을 함수를 이용해 만들자
# '''
# 사용자가 숫자 2개를 입력하고 연산자를 선택하면, 연산결과가 출력되는 프로그램은
# 함수를 이용해서 만들어보자
# '''

# # (이전까지 수행했던, 일종의 '하드코딩' 방식)
# def calculator():
#     if selectedOperator == 1:           #덧셈
#         print(f'덧셈의 결과: {inputNumber1 + inputNumber2}')

#     elif selectedOperator == 2:         #뺄셈
#         print(f'뺄셈의 결과: {inputNumber1 - inputNumber2}')

#     elif selectedOperator == 3:         #곱셈
#         print(f'곱셈의 결과: {inputNumber1 * inputNumber2}')

#     elif selectedOperator == 4:         #나눗셈
#         print(f'나눗셈의 결과: {inputNumber1 / inputNumber2}')



# # (1개의 함수 내부의 수식들 또한 함수로 만들어서 단순/간결하게 만듬)
# def add():
#     print(f'덧셈의 결과: {inputNumber1 + inputNumber2}')

# def sub():
#     print(f'뺄셈의 결과: {inputNumber1 - inputNumber2}')

# def mul():
#     print(f'곱셈의 결과: {inputNumber1 * inputNumber2}')

# def div():
#     print(f'나눗셈의 결과: {inputNumber1 / inputNumber2}')



# def calculator():
#     if selectedOperator == 1:           #덧셈
#         add()

#     elif selectedOperator == 2:         #뺄셈
#         sub()

#     elif selectedOperator == 3:         #곱셈
#         mul()

#     elif selectedOperator == 4:         #나눗셈
#         div()


# inputNumber1 = float(input('첫 번째 숫자 입력: '))
# selectedOperator = int(input('연산자 선택 - 1.덧셈    2.뺄셈    3.곱셈    4.나눗셈'))
# inputNumber2 = float(input('두 번째 숫자 입력: '))

# calculator()

# 1개의 함수에는 1개의 기능을 담을 것(1개 함수에 2개 이상의 기능을 담믐 것은 지양할 것)
# 최대한 가능한 만큼 부품화(부분 모듈화) 하는게 이상적이다


# TDD(Test-Driven-Development): 개발방법론(테스트 주도 개발)
# 실제 코드를 개발하기 전에, 테스트 케이스를 먼저 작성하는 소프트웨어 개발 방법론
# [실패하는 테스트 작성(Red) -> 테스트 통과 토드 작성(Green) -> 리팩토링(Blue)]의 
# 짧은 주기를 반복해 고품질의 버그 없는 코드를 완성하는 방식


