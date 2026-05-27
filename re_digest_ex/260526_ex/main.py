# quiz) - 가위, 바위, 보 게임
'''
컴퓨터와 함께하는 가위 바위 보 게임을 만들자, 난수를 이용해 게임을 진행하고 결과를 출력한다

가위 바위 보를 선택하세요.
0.가위 1.바위 2.보 :: 0
Com : 바위
User : 가위
컴퓨터 승리
'''

# main.py : 실행 파일


import temp     #함수를 담은 모듈 파일을 소환(import)한다

selects = []    #(사용자가) 선택한 것을 담는 []리스트

inputData = (int(input('가위 바위 보를 선택하세요 0.가위   1.바위   2.보')))
#inputData에 할당한다, 사용자가 선택할 "0.가위   1.바위   2.보"의 데이터(input)를 정수(int)로 캐스팅해서
selects.append(inputData)   #(사용자가) 선택한 것을 담는 []에 추가한다, 사용자가 선택할 데이터(inputData)를


temp.setUSelecNumbers(selects)  #모듈. set한다,user가 selec한 numbers를(사용자가 선택한 것을 담는 리스트)
temp.setRNumbers()              #함수. set한다,r(랜덤)한 numbers를

print(f'Computer 선택: {temp.getRNumbers()}')
#출력한다, (f'com선택: {모듈.'get한다,r(랜덤)한 numbers를'}')
print(f'User 선택: {temp.getUSelecNumbers()[0]}')
#출력한다, (f'user선택: {모듈.'get한다,user가 selec한 numbers를'}')
print(f'가위바위보 결과: {temp.compareNumbers()[0]}')
#출력한다, (f'com난수와 user정수의 비교결과: {모듈.'compare(비교)한다,난수와 정수를'}')

