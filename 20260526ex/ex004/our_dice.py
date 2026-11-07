import random

class Dice:
    '''주사위를 굴린 결과를 모아 두는 클래스.'''

    def __init__(self):
        self.numbers = []

    def playDice(self):
        '''1~6 사이 숫자를 하나 뽑아 numbers 에 추가한다.'''
        self.numbers.append(random.randint(1, 6))

    def getNumbers(self):
        '''지금까지 나온 숫자 목록을 돌려준다.'''
        return self.numbers
    
    def getSum(self):
        '''지금까지 나온 숫자의 합을 돌려준다.'''
        return sum(self.numbers)
