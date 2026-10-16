# quiz - lotto game

import random

userNums = []
randNums = []
collect = []

def setUNumbers(ns):      # setter: 세팅하는 함수(= set + userNums/uNumbers)
    '''사용자가 고른 로또 번호 목록을 저장한다.'''
    global userNums
    userNums = ns

def getUNumbers():       # getter: 데이터를 조회하는 함수(= get + userNums/uNumbers)
    '''저장된 사용자 번호 목록을 반환한다.'''
    return userNums

def setRNumbers():
    '''1~45 중 중복 없이 6개를 뽑아 당첨 번호로 저장한다.'''
    global randNums
    randNums = random.sample(range(1, 46), 6)

def getRNumbers():
    '''저장된 당첨 번호 목록을 반환한다.'''
    return randNums

def compareNumbers():
    '''사용자 번호 중 당첨 번호와 일치하는 번호 목록을 반환한다.'''
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)
    
    return collect

