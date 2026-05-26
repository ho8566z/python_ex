# quiz) - 가위, 바위, 보 게임
'''
컴퓨터와 함께하는 가위 바위 보 게임을 만들자, 난수를 이용해 게임을 진행하고 결과를 출력한다

가위 바위 보를 선택하세요.
0.가위 1.바위 2.보 :: 0
Com : 바위
User : 가위
컴퓨터 승리
'''

import temp

selects = []

selects.append(int(input('가위 바위 보를 선택하세요 0.가위   1.바위   2.보')))

temp.setUSelecNumbers(selects)
temp.setRNumbers()

print(f'Computer 선택: {temp.getRNumbers()}')
print(f'User 선택: {temp.getUSelecNumbers()}')
print(f'가위바위보 결과: {temp.compareNumbers()}')
