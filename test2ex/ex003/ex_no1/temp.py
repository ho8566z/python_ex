# quiz) - 가위, 바위, 보 게임
'''
컴퓨터와 함께하는 가위 바위 보 게임을 만들자, 난수를 이용해 게임을 진행하고 결과를 출력한다

가위 바위 보를 선택하세요.
0.가위 1.바위 2.보 :: 0
Com : 바위
User : 가위
컴퓨터 승리
'''

import random

userSelectedNums = []
randNums=[]
collects = []

def setUSelecNumbers(ns):
    global userSelectedNums
    userSelectedNums = ns

def getUSelecNumbers():
    return userSelectedNums

def setRNumbers():
    global randNums
    randNums = random.randrange(3)

def getRNumbers():
    return randNums

def compareNumbers():
    global userSelectedNums
    global randNums
    global collects

    collects = []

    result = ""

    if randNums == userSelectedNums:
        result = '비겼습니다.'
    elif (randNums==0 and userSelectedNums==2) or (randNums==1 and userSelectedNums==0) or (randNums==2 and userSelectedNums==1):
        result = '졌습니다.'
    elif (randNums==0 and userSelectedNums==1) or (randNums==1 and userSelectedNums==2) or (randNums==2 and userSelectedNums==0):
        result = '이겼습니다.'

    print(result)
    collects.append(result)

    return collects