import random

# 주사위를 굴린 결과를 모아 두는 클래스
class Dice:
    def __init__(self):
        self.numbers = []

    # 1~6 사이 숫자를 하나 뽑아 numbers 에 추가한다.
    def playDice(self):
        self.numbers.append(random.randint(1, 6))

    # 지금까지 나온 숫자 목록을 돌려준다.
    def getNumbers(self):
        return self.numbers
    
    # 지금까지 나온 숫자의 합을 돌려준다.
    def getSum(self):
        return sum(self.numbers)
