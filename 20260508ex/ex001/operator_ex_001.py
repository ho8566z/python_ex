'''
# quiz
# 수심10 내려갈때 마다 0.7도씩 수온이 감소함
# 수면(수심0m)의 온도는 20도

data = float(input('수심을 입력하세요. '))
temperature = 20 - (data // 10 * .7)
print(f'temperature: {temperature}')


# quiz2
# 속도와 시간을 통해 자동차의 주행거리를 구하자

speedData = input('주행 속도: ')
timeData = input('주행 시간: ')
distance = int(speedData) * float(timeData)
print(f'주행 거리: {distance}')


# quiz3
# A회사는 3대의 컴퓨터로 8시간을 일하면 하루 업무를 처리할 수 있다.
# 그런데 단축근무를 하게되어 근무시간이 줄게 되면
# 몇대의 컴퓨터가 필요한지?
# 근무시간을 입력하면 필요한 컴퓨터 수량을 파악하는 프로그램을 만들자

# workTime = 3 * 8 = 24
# workTime = 24 / 8 = 3

workTime = int(input('근무시간을 입력하세요. '))
computer = 3 * 8 // workTime
addComputer = 1 if (3 * 8 % workTime) > 0 else 0
totalComputer = computer + addComputer
print(f'필요한 컴퓨터 개수는: {totalComputer}')


# 마스크(340원)의 구매 개수에 따른 거스름돈 지불 프로그램

maskPrice = 340
maskCnt = int(input('마스크 구매 개수: '))
totalPrice = maskPrice * maskCnt
cash = int(input('지불 금액: '))
change = cash - totalPrice
print(f'거스름돈: {change}')


# 13시 30분 25초를 프로그램으로
print(f'second: {25 + (60 * 30) + (60 * 60 * 13)}')
#second: 48625


# 학생의 국어, 영어, 수학 점수를 입력하면 총점과 평균을 출력하자
kor = float(input('국어 점수: '))
eng = float(input('영어 점수: '))
mat = float(input('수학 점수: '))

totalScore = kor + eng + mat
averageScore = totalScore / 3
print(f'totalScore: {totalScore}')
print(f'averageScore: {averageScore}')


# 밤 최저 기온과 낮 최고 기온을 입력하면 일교차를 출력하는 프로그램

afterTemp = float(input('낮 최고 기온: '))
nightTemp = float(input('밤 최저 기온: '))
tempGap = afterTemp - nightTemp
print(f'일교차: {tempGap}')

highTemp = float(input('낮 최고 기온: '))
lowTemp = float(input('밤 최저 기온: '))
tempGap = highTemp - lowTemp
print(f'일교차: {tempGap}')
'''

# 사용자가 길이(cm)를 입력하면 inch로 환산하는 프로그램
# (단 , 1cm는 0.391inch로 한다)

cm = float(input('길이를 입력하세요. (cm)'))
#길이를 입력하세요. (cm)11.1
inch = 0.39 * cm
print(f'inch: {inch}') #inch: 4.329
