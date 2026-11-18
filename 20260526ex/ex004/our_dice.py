'''주사위를 굴려 나온 숫자를 모으고 합계를 구하는 Dice 클래스 모듈.'''
import random

class Dice:
    '''주사위를 굴린 결과를 모아 두는 클래스.'''

    def __init__(self):
        '''주사위에서 나온 숫자를 담을 빈 리스트를 만든다.'''
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
