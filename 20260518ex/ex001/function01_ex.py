# # quiz - 상품가격표를 참조해서 실행결과를 참조해서 영수증을 출력하는 함수를 만들자
# # 단, 살품개수는 사용자가 입력한다

# goods = {
#     '새우깡': 1200,
#     '비비빅': 400,
#     '초코파이': 500,
#     '맛동산': 1500
# }

# totalPrice = 0


# def shrimpCrackersPrie():
#     global totalPrice
#     totalPrice += goods['새우깡'] * shrimpCrackers
#     print(f'새우깡 구매 금액: {goods['새우깡'] * shrimpCrackers}원')

# def bibibigsPrie():
#     global totalPrice
#     totalPrice += goods['비비빅'] * bibibigs
#     print(f'비비빅 구매 금액: {goods['비비빅'] * bibibigs}원')

# def chocolletPiesPrie():
#     global totalPrice
#     totalPrice += goods['초코파이'] * chocolletPies
#     print(f'초코파이 구매 금액: {goods['초코파이'] * chocolletPies}원')

# def matdongsanPrie():
#     global totalPrice
#     totalPrice += goods['맛동산'] * matdongsan
#     print(f'맛동산 구매 금액: {goods['맛동산'] * matdongsan}원')


# shrimpCrackers = int(input('새우깡 구매 개수: '))
# bibibigs = int(input('비비빅 구매 개수: '))
# chocolletPies = int(input('초코파이 구매 개수: '))
# matdongsan = int(input('맛동산 구매 개수: '))
# print('=' * 40)


# shrimpCrackersPrie()
# bibibigsPrie()
# chocolletPiesPrie()
# matdongsanPrie()
# print('=' * 40)

# print(f'총 구매 금액: {totalPrice}')
# print('=' * 40)

# # 새우깡 구매 개수: 10
# # 비비빅 구매 개수: 20
# # 초코파이 구매 개수: 30
# # 맛동산 구매 개수: 40
# # ========================================
# # 새우깡 구매 금액: 12000원
# # 비비빅 구매 금액: 8000원
# # 초코파이 구매 금액: 15000원
# # 맛동산 구매 금액: 60000원
# # ========================================
# # 총 구매 금액: 95000
# # ========================================


# 지역변수 & 전역변수
# 변수의 범위(scope)에 따라 구분됨

# 지역변수
# 1. 선언된(만들어진) 함수, 블록 안에서만 유효하며, 함수 바깥의 외부에서는 
# 해당 변수에 대한 접근이 불가능함
# 2. 프로그램 실행 중 해당 블록이나 함수가 호출될 때, 메모리에 생성되고, 작업이
# 종료하면 즉시 사라진다

# 전역변수
# 1. 프로그램이 시작될때 생성되고 종료할때 소멸한다
# 2. 코드 내의 모든 함수나 변수에서 별도의 전달 등이 없어도 자유롭게 공유가 가능함

# 지역변수 and 전역변수
# 함수 내에 지역변수와 함수 바깥의 전역변수가 동시에 존재할때, 지역변수를 우선
# 순위로서 사용한다


# global키워드
# 함수 내부에서 전역변수를 수정할 때, global 키워드를 사용한다
# 기본적으로 함수 내부에 값을 대입하면, 파이썬에서는 해당 변수를 '지역변수'로서 
# 인식하고 error가 발생한다(전역변수에서 찾는 시도도 없음)

# (함수 내, 최상단에 'global키워드' X)
# count = 0

# def increase():
#     count = count + 1
#     print(count)

# increase()
# # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value

# (함수 내, 최상단에 'global키워드' O)
# count = 0

# def increase():
#     global count	  #'count'는 지역변수가 아닌, 전역변수라고 인식시키는 과정
#     count = count + 1
#     print(count)

# increase()          #1



# student = {
#     '이름': '홍길동',
#     '나이': 25
# }

# print(f'나이: {student['나이']}')       #나이: 25

# def modifyStudentAge():
#     student['나이'] += 1

# modifyStudentAge()

# print(student['나이'])                 #26

