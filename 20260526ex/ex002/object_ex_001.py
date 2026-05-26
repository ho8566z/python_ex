# 객체 지향 프로그래밍: OOP(Object-Oriented-Programming)

# 컴퓨터 프로그램을 명령어의 단순한 나열(:절차 지향 프로그래밍)로 보는 대신, 
# '객체'라는 독립된 작은 단위들의 모임으로 파악하고 객체들이 서로 상호작용하도록 만드는 개발 방법론
# -> 현실 세계의 사물이나 개념을 소프트웨어 안으로 녹여내기 위해 고안된 방식

# 객체(object): 세상에 존재하는 사람, 사물 등의 모든 형체가 있는 것이며, 속성과 기능으로 구성된다
# (사물ex: 키보드, 모니터 등등)
# 속성(attribute): 객체를 구성하는 요소(ex: 크기, 무게, 부피, 색상 등등)
# 기능(function): 객체가 하는 행위(ex: 걷는다, 말한다, 클릭한다 등등)

# 객체(object) = 속성(attribute) + 기능(function)


# ex) 계산기
# 객체: 계산기, 속성: 사용자로 부터 입력받은 숫자, 기능: 덧셈, 뺄셈, 곱셈, 나눗셈 등


# 객체 + 객체
# 객체는 단독으로도 사용되기도 하지만, 서로 유기적으로 관계를 맺고 사용되기도 한다
# 계산 프로그램에서 '계산기'라는 객체와 '프린트'객체가 서로 유기적으로 관계를 맺어서 입력받은 숫자를 계산하고, 
# 프린트되는 방식으로 결과가 이루어진다

# 객체 지향 프로그래밍: 우리가 만드는 프로그램을 객체 단위로 구분하고, 각각의 객체를 서로 연관지어서 부품을 
# 조립하여서 유기적인 동작을 하도록 하는 프로그래밍 패러다임이다


# 클래스(Class): 객체를 만들기 위한 틀/설계도
# ex) 붕어빵 틀(=클래스) -> 붕어빵(=객체)

# 동일한 클래스를 통해 만들어진 객체라도 서로 완전히 같을 수 없으며, 전혀 다르게 독립적으로 인식된다


# 클래스의 구조

# -> class선언
# class FishBread: (class키워드 + class이름:)
# # 클래스 이름은 함수와 구분하기 위해 소문자가 아닌, 대문자로 시작

# -> 클래스 속성 정의
# def __init__(self, f, b):
#   self.flour = f
#   self.bean = b
# # -> '__init__': '변수 선언 및 초기화'와 같이 메모리를 청소해
# # 메모리를 사용할 준비를 하는 과정(=클래스 선언)
# # self 키워드는 클래스 자신을 가리킨다는 의미를 지님
# # (-> 첫번재 매개변수는 무조건 self)

# -> 클래스 기능
# def makeFishBread(self):
#   print('붕어빵 제조')
# # 함수 'makeFishBread()'또한 self를 사용해야 'FishBread'클래스 내부에서 기능한다


# 클래스 문법(객체를 만듥기 위한 틀/설계도)

# class FishBread:    #클래스 선언
#     # 속성(attribute) 정의
#     def __init__(self, f, b):
#         self.flour = f
#         self.bean = b
        
#     # 기능(function, method) 정의
#     def makeFishBread(self):
#         print('붕어빵 제조')



# # 계산기 클래스
# class Calculator:
#     #속성
#     def __init__(self, n1, n2):
#         self.num1 = n1
#         self.num2 = n2

#     #기능
#     def add(self):
#         print(f'add: {self.num1 + self.num2}')

#     def sub(self):
#         print(f'sub: {self.num1 - self.num2}')

#     def mul(self):
#         print(f'mul: {self.num1 * self.num2}')

#     def div(self):
#         print(f'div: {self.num1 / self.num2}')



# # 인간 클래스
# class Human:
#     #속성
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight

#     #기능
#     def walk(self):
#         print('걷다')
    
#     def run(self):
#         print('뛰다')

#     def printMyInfo(self):
#         print(f'나의 신장: {self.height}')
#         print(f'나의 체중: {self.weight}')




# # 붕어빵 클래스로부터 객체를 만들어 보자(객체 생성)

# class FishBread:    #클래스 선언
#     # 속성(attribute) 정의
#     def __init__(self, f, b):
#         self.flour = f
#         self.bean = b
        
#     # 기능(function, method) 정의
#     def makeFishBread(self):
#         print('붕어빵 제조')

# # 실행 ex)
# myFishBread = FishBread('팥', '밀가루')
# friendFishBread = FishBread('호박', '쌀')
# hisFishBread = FishBread('꿀', '밀가루')

# print(f'나의 붕어빵의 속 내용물: {myFishBread.flour}')
# print(f'나의 붕어빵의 반죽: {myFishBread.bean}')
# print(f'친구의 붕어빵의 속 내용물: {friendFishBread.flour}')
# print(f'친구의 붕어빵의 반죽: {friendFishBread.bean}')
# print(f'그의 붕어빵의 속 내용물: {hisFishBread.flour}')
# print(f'그의 붕어빵의 반죽: {hisFishBread.bean}')
# #나의 붕어빵의 속 내용물: 팥
# #나의 붕어빵의 반죽: 밀가루
# #친구의 붕어빵의 속 내용물: 호박
# #친구의 붕어빵의 속 내용물: 쌀
# #그의 붕어빵의 속 내용물: 꿀
# #그의 붕어빵의 속 내용물: 밀가루



# # 계산기 클래스(객체 생성)
# class Calculator:
#     #속성
#     def __init__(self, n1, n2):
#         self.num1 = n1
#         self.num2 = n2

#     #기능
#     def add(self):
#         print(f'add: {self.num1 + self.num2}')

#     def sub(self):
#         print(f'sub: {self.num1 - self.num2}')

#     def mul(self):
#         print(f'mul: {self.num1 * self.num2}')

#     def div(self):
#         print(f'div: {self.num1 / self.num2}')
    
# myCalculator = Calculator(10, 20)
# myCalculator.add()      #add: 30
# myCalculator.sub()      #sub: -10
# myCalculator.mul()      #mul: 200
# myCalculator.div()      #div: 0.5

# frindcalculator = Calculator(100, 200)
# frindcalculator.add()   #add: 300
# frindcalculator.sub()   #sub: -100
# frindcalculator.mul()   #mul: 20000
# frindcalculator.div()   #div: 0.5\



# # 인간 클래스(객체 생성)
# class Human:
#     #속성
#     def __init__(self, height, weight):
#         self.height = height
#         self.weight = weight

#     #기능
#     def walk(self):
#         print('걷다')
    
#     def run(self):
#         print('뛰다')

#     def printMyInfo(self):
#         print(f'나의 신장: {self.height}')
#         print(f'나의 체중: {self.weight}')

# human1 = Human(188, 87)
# human2 = Human(165, 49)

# human1.printMyInfo()    #188, 87
# human2.printMyInfo()    #165, 49

# human1 = human2
# human1.printMyInfo()    #165, 49

# human1.height = 200
# human1.weight = 39

# human2.printMyInfo()    #200, 39
# # (human2의 데이터를 human1가 가리키게 되었기 때문에 human1의 데이터를 바꾸면, 
# # human2의 데이터 또한 변경된다)

# Gemini Said: 'human1 = human2'는 데이터를 복사하는 것이 아니라
# "너도 내가 보고 있는 거 같이 보자"라고 주소를 공유하는 명령이다


