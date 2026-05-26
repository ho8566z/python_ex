# quiz - lotto game

import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns):      # setter: 세팅하는 함수(= set + userNums/uNumbers)
    global userNums
    userNums = ns

def getUNumbers():       # getter: 데이터를 조회하는 함수(= get + userNums/uNumbers)
    return userNums

def setRNumbers():
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)
    
    return collect

