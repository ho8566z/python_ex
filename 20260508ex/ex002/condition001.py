# 조건문(if문)

'''
if 조건식:
    실행문
'''

# num = 50
# if num > 10:
#     print('num은 10보다 크다--') #실행
#     print('num은 10보다 크다--') #실행
# print('num은 10보다 크다++') #'들여쓰기'가 아님 = 코드 블록x
# #num은 10보다 크다 (10보다 큰 경우에만)

# num = 5
# if num > 10:
#     print('num은 10보다 크다--') #실행 불가
#     print('num은 10보다 크다--') #실행 불가
# print('num은 10보다 크다++') #'들여쓰기'가 아님 = 코드 블록x
# #num은 10보다 크다 (10보다 큰 경우에만)

'''
if키워드: 조건문을 선언하기 위한 키워드로 '만약 ~라면' 의 뜻을 가짐
조건식: 특정 조건을 기술한다. 조건식의 결과에 따라 실행문의 실행 여부가 결정됨
콜론: 코드 블록의 시작을 나타내는 것으로 콜론 이후부터가 실행될 문장이다
실행문: 조건식의 결과가 침(True)인 경우, 실행하는 명령문이다
       조건식의 결과가 거짓(False)인 경우, 실행문은 실행되지 않음
'''

'''
# # 사용자가 입력힌 정수가 10보다 크면 실행문을 출력하는 프로그램
# num = int(input('pleasee input intege number'))

if num > 10:
    print(f'{num}은 10보다 크다.')

if num == 10:
    print(f'{num}은 10과 같다.')

if num < 10:
    print(f'{num}은 10보다 작다.')


# quiz(속도위반 경고)
# 제한 속도가 50km/h인 도로에서 속도위반을 하는 자동차에 경고를 하는 프로그램

speed = int(input('현재 속도: '))
speedLim = 50

if speed < 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 느리다')

if speed == 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h과 같다')

if speed > 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 빠르다')


# import random
# randomNum = random.randrange(1, 46)
# print(f'randomNum: {randomNum}')
import random
speed = random.randrange(1, 101)
speedLim = 50

if speed < 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 느리다')

if speed == 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h과 같다')

if speed > 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 빠르다')


#코드블록이 1개라면 개행하지 않아도 실행 가능

speed = int(input('현재 속도: '))
speedLim = 50

if speed < 50:
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 느리다')
    print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 느릴까?')

if speed == 50: print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h과 같다')

if speed > 50:print(f'현재 속도는 {speed}km/h로 제한 속도인 {speedLim}km/h보다 빠르다')
'''

# num = 50
# if num > 0:
#     pass

# num = 50
# if num > 0:
#     print(f'num은 0보다 크다')

#     print(f'---------------------------')

#     print(f'num은 0보다 크다')

'''
# if ~ else 구문 -> 양자택일의 상황에만 사용할 것
# else: 그렇지 않으면~

myScore = 75
if myScore >= 80:
    print(f'생존')

if myScore < 80:
    print(f'탈락')


myScore = 75
if myScore >= 80:
    print(f'생존')
else:
    print(f'탈락')
'''

# if ~ elif 구문 -> 다중선택의 상황에 사용
'''
점수가 90점 이상이면 'A'학점 출력,
점수가 80점 이상 ~ 90점 미만이면 'B'학점 출력,
점수가 70점 이상 ~ 80점 미만이면 'C'학점 출력,
점수가 60점 이상 ~ 70점 미만이면 'D'학점 출력,


myScore = float(input('점수 입력: '))
if myScore >= 90:
    print('A')
elif myScore >= 80:
    print('B')
elif myScore >= 70:
    print('C')
elif myScore >= 60:
    print('D')
else:
    print('F')
'''


# myScore = float(input('점수 입력: '))
# if myScore >= 90:
#     print('A')
# elif myScore >= 70 and (myScore < 80): #70이상 80미만
#     print('C')
# elif myScore >= 80 and (myScore < 90): #80이상 90미만
#     print('B')
# elif myScore >= 60 and (myScore < 70): #60이상 70미만
#     print('D')
# else:
#     print('F')


# quiz 자동주문 시스템 개발
'''
다국어를 지원하는 식당에서 사용할 자동주문 시스템을 만들자
1번을 누르면 한국어로, 2번을 누르면 영어로, 3번을 누르면 중국어로,
그 외 번호를 누르면 영어로 주문을 받는 프로그램

1.대한민국     2.USA     3.中國
1: 주문하시겠습니까?
2: Would you like to order?
3: 您想下单吗？
그외: Would you like to order?


order = int(input('원하는 언어를 선택하세요(1:한글 / 2:english / 3:中國語)'))

if order == 1:
    print('주문하시겠습니까?')
elif order == 2:
    print('Would you like to order?')
elif order == 3:
    print('您想下单吗？')
else:
    print('Would you like to order?')


selectNumber = int(input('1.대한민국     2.USA     3.中國'))
if selectNumber == 1:
    print('주문하시겠습니까?')
elif selectNumber == 2:
    print('Would you like to order?')
elif selectNumber == 3:
    print('您想下单吗？')
else:
    print('Would you like to order?')
'''

# KOREA_NUMBER = 1
# USA_NUMBER = 2
# CHINA_NUMBER = 3

# selectNumber = int(input('1.대한민국     2.USA     3.中國'))

# if selectNumber == KOREA_NUMBER:
#     print('주문하시겠습니까?')
# elif selectNumber == USA_NUMBER:
#     print('Would you like to order?')
# elif selectNumber == CHINA_NUMBER:
#     print('您想下单吗？')
# else:
#     print('Would you like to order?')


# quiz 국가재난지원금 수령액 조회
'''
다음은 가구인원수에 따른 국가재난지원금 수령액을 안내하는 프로그램
표를 참고해 프로그램 제작하자
1인 가구: 400,000원
2인 가구: 600,000원
3인 가구: 800,000원
4인 가구이상: 1,000,000원


FAMILY_1PEOPLE = 1
FAMILY_2PEOPLE = 2
FAMILY_3PEOPLE = 3
FAMILY_4PEOPLE_OVER = 4

selectPeople = int(input('가구원 수를 선택하세요[1. 1인가구   2. 2인가구   3. 3인가구   4. 4인가구 이상]'))
if selectPeople == FAMILY_1PEOPLE:
    print('해당 가구의 국가재난지원금 수령액은 400,000원 입니다')
elif selectPeople == FAMILY_2PEOPLE:
    print('해당 가구의 국가재난지원금 수령액은 600,000원 입니다')
elif selectPeople == FAMILY_3PEOPLE:
    print('해당 가구의 국가재난지원금 수령액은 800,000원 입니다')
elif selectPeople == FAMILY_4PEOPLE_OVER:
    print('해당 가구의 국가재난지원금 수령액은 1,000,000원 입니다')   
else:
    print('해당 가구의 국가재난지원금 수령액은 1,000,000원 입니다')
'''


# quiz

'''
다음 요구사항을 충족하는 프로그램을 if~elif문을 이용해 만들자
-BMI 지수를 입력한다
-BMI 지수가 90 이하면 '저체중'을 출력한다
-BMI 지수가 90 초과~110 이하면 '정상 체중'을 출력한다
-BMI 지수가 110 초과~120 이하면 '과체중'을 출력한다
-BMI 지수가 120 초과~140 이하면 '비만'을 출력한다
-BMI 지수가 140 초과면 '고도 비만'을 출력한다


BMI_SLIM = 90
BMI_LITTLE_SLIM = 110
BMI_LITTLE_FAT = 120
BMI_FAT = 140

myWeight = float(input('당신의 체중을 입력하세요. '))
if myWeight <= BMI_SLIM:
    print('저체중')
elif (myWeight > BMI_SLIM) and (myWeight <= BMI_LITTLE_SLIM):
    print('정상 체중')
elif (myWeight > BMI_LITTLE_SLIM) and (myWeight <= BMI_LITTLE_FAT):
    print('과체중')
elif (myWeight > BMI_LITTLE_FAT) and (myWeight <= BMI_FAT):
    print('비만')
else:
    print('고도 비만')
'''


# 중첩 조건문               ((((# ai 질문할 것))))
# 조건문 내에 또 다른 조건문을 쓸 수 있는데, 이를 중첩 조건문이라 한다
# 사용자가 입력한 정수에서 양수(0도 포함)인지를 판단하고 양수라면 홀/짝 구분하자
'''
myInteger = int(input('정수 입력 '))
if myInteger > 0:
    print('양수')
    if myInteger % 2 == 0:
        print('짝수')
    else:
        print('홀수')
elif myInteger == 0:
    print('0')
else:
    print('음수')
'''

# 홀/짝을 판단하는 프로그램을 만들자
'''
num = int(input('양수를 입력하세요 '))
if num > 0:
    if num % 2 == 0:
        print('입력한 정수는 짝수입니다')
    else:
        print('입력한 정수는 홀수입니다')
else:
    print('입력한 정수는 0또는 음수입니다')
'''

# quiz
'''
출생연도 끝자리(endBirthYear)와 나이(age)를 입력하면 다음 요구사항에 맞춰
마스크 구매가 가능한 요일을 출력하는 프로그램

-공적마스크 판매 관련해서 출생연도 끝자리를 이용한 5부제를 다음과 같이 실시
    -1,6 => 월
    -2,7 => 화
    -3,8 => 수
    -4,9 => 목
    -5,0 => 금
    -만 65세 이상은 언제든지 가능


endBirthYear = int(input('출생연도 끝자리 입력: '))
age = int(input('나이 입력: '))

if age < 65:
    if endBirthYear == 1 or endBirthYear == 6:
        print('월요일에 구매가능합니다')
    elif endBirthYear == 2 or endBirthYear == 7:
        print('화요일에 구매가능합니다')
    elif endBirthYear == 3 or endBirthYear == 8:
        print('수요일에 구매가능합니다')
    elif endBirthYear == 4 or endBirthYear == 9:
        print('목요일에 구매가능합니다')
    elif endBirthYear == 5 or endBirthYear == 0:
        print('금요일에 구매가능합니다')

else:
    print('언제든지 가능')
'''


# 날짜 관련 모듈: datetime
# import operator과는 다름

from datetime import datetime

# 현재 '일'을 구하기
# print(datetime.today().day)


# quiz (차량 2부제 프로그램)
toDayNo = datetime.today().day

carNum = int(input('당신의 차량번호를 입력하세요. '))
print(f'오늘은 {toDayNo}일 입니다')

if carNum % 2 == 0:
    if toDayNo % 2 == 0:
        print('당신의 차량을 입차 가능합니다.')
    elif toDayNo % 2 != 0:
        print('당신의 차량을 입차 불가능합니다.')

if carNum % 2 != 0:
    if toDayNo % 2 == 0:
        print('당신의 차량을 입차 불가능합니다.')
    elif toDayNo % 2 != 0:
        print('당신의 차량을 입차 가능합니다.')



'''
# quiz (생존율 출력 프로그램)

최초 시행시간에 따른 생존율 변화
 -60초 = 85%
 -120초 = 76%
 -180초 = 66%
 -240초 = 57%
 -300초 = 47%
 -300초 초과 = 25% 미만


startUseTime = int(input('최초 시행까지 걸린 시간: '))
# startUseTime = lifeGoldenTime

if startUseTime <= 60:
    print('생존율은 85% 입니다.')
elif startUseTime <= 120:
    print('생존율은 76% 입니다.')
elif startUseTime <= 180:
    print('생존율은 66% 입니다.')
elif startUseTime <= 240:
    print('생존율은 57% 입니다.')
elif startUseTime <= 300:
    print('생존율은 47% 입니다.')
else:
    print('생존율은 25% 미만입니다.')
'''

'''
# quiz (전기 요금 계산기)
# 전기를 사용함에 따라서 누진세가 붙고, 단가와 기본요금이 올라간다
# 누진세 전기표를 통해 전기 사용량을 입력하면, 전기료가 출력되는 프로그램


 -사용량:200이하 = 단가(원):99.3 = 기본요금(원):910
 -사용량:201~400이하 = 단가(원):187.9 = 기본요금(원):1600
 -사용량:400초과 = 단가(원):280.6 = 기본요금(원):7300


electricUse = float(input('전기 사용량을 입력하세요. '))
print(f'당신의 전기 사용량은 {electricUse}kwh 입니다.')

if electricUse <= 200.0:
    print(f'당신의 기본요금은 910원 입니다. ')
    print(f'당신의 전기 사용단가는 99.3원 입니다. ')
    print(f'당신의 전기요금은 {910 + (electricUse * (99.3)):.2f}입니다.')
elif electricUse > 201 and electricUse <= 400:
    print(f'당신의 기본요금은 1,600원 입니다. ')
    print(f'당신의 전기 사용단가는 187.9원 입니다. ')
    print(f'당신의 전기요금은 {1600 + (electricUse * (187.9)):.2f}입니다.')
else:
    print(f'당신의 기본요금은 7300원 입니다. ')
    print(f'당신의 전기 사용단가는 280.6원 입니다. ')
    print(f'당신의 전기요금은 {7300 + (electricUse * (280.6)):.2f}입니다.')
'''

''''
kwh = int(input('전기 사용량을 입력하세요. '))
price = 0
basic = 0

if kwh <= 200:
    price = 99.3
    basic = 910
elif kwh <= 400:
    price = 187.9
    basic = 1600
else:
    price = 7300
    basic = 280.6

totalPrice = int(basic + (kwh * price))

print(f'당신의 전기요금은 {totalPrice:.2f}원 입니다.')
'''

'''
# 삼항 연산자를 활용한 if~else문 프로그램

myScore = int(input('시험점수 입력: '))
targetScore = 85

result = 'succes' if myScore >= targetScore else 'fail'
print(f'result: {result}')
'''


'''
import random
ranNum = random.randint(1, 3)

myNum = int(input('1.가위 2.바위 3.보 중에 선택하세요. '))

if ranNum == 1 and myNum == 1:
    print('무승부')
elif ranNum == 1 and myNum == 2:
    print('사용자 승')
elif ranNum == 1 and myNum == 3:
    print('컴퓨터 승')

elif ranNum == 2 and myNum == 1:
    print('컴퓨터 승')
elif ranNum == 2 and myNum == 2:
    print('무승부')
elif ranNum == 2 and myNum == 3:
    print('사용자 승')

elif ranNum == 3 and myNum == 1:
    print('사용자 승')
elif ranNum == 3 and myNum == 2:
    print('컴퓨터 승')
elif ranNum == 3 and myNum == 3:
    print('무승부')
'''

'''
import random
ranNum = random.randint(1, 3)

myNum = int(input('1.가위 2.바위 3.보 중에 선택하세요. '))

if (ranNum == 1 and myNum == 1) or \
    (ranNum == 2 and myNum == 2) or \
    (ranNum == 3 and myNum == 3):
    print('무승부')
elif (ranNum == 1 and myNum == 2) or \
    (ranNum == 2 and myNum == 3) or \
    (ranNum == 3 and myNum == 1):
    print('사용자 승')
elif (ranNum == 1 and myNum == 3) or \
    (ranNum == 2 and myNum == 1) or \
    (ranNum == 3 and myNum == 2):
    print('컴퓨터 승')
'''

'''
import random
ranNum = random.randint(1, 3)

myNum = int(input('1.가위 2.바위 3.보 중에 선택하세요. '))

if (ranNum == 1 and myNum == 2) or \
    (ranNum == 2 and myNum == 3) or \
    (ranNum == 3 and myNum == 1):
    print('사용자 승')
elif (ranNum == 1 and myNum == 3) or \
    (ranNum == 2 and myNum == 1) or \
    (ranNum == 3 and myNum == 2):
    print('컴퓨터 승')
elif ranNum == myNum:
    print('무승부')
'''


# quiz
'''
사용자가 입력한 문자 메세지의 길이에 따라서 SMS 또는 MMS의 발송을 결정하는 프로그램
(단, 메세지 길이가 50 이하면 SMS 발송, 그렇지 않으면 MMS 발송)


# str = 'hello   '
# print(f'str: {str}')
# print(f'str\'s lsngth: {len(str)}')

useMessage = int(input('메세지를 입력하세요. '))
msgLen = len(useMessage)

if msgLen <= 50:
    print('SMS 발송')
else:
    print('MMS 발송')
'''