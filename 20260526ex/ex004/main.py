from our_dice import Dice

def sortNumbers(*numbers):
    list = sorted(numbers)
    list.sort(reverse=True)
    return list

gamer1Dice = Dice()
gamer2Dice = Dice()
gamer3Dice = Dice()

for i in range(5):
    gamer1Dice.playDice()
    gamer2Dice.playDice()
    gamer3Dice.playDice()

print(f'gamer1: {gamer1Dice.getNumbers()}')
print(f'gamer2: {gamer2Dice.getNumbers()}')
print(f'gamer3: {gamer3Dice.getNumbers()}')

print(f'sum of gamer1: {gamer1Dice.getSum()}')
print(f'sum of gamer2: {gamer2Dice.getSum()}')
print(f'sum of gamer3: {gamer3Dice.getSum()}')

sortedNumbers = sortNumbers(gamer1Dice.getSum(),
                            gamer2Dice.getSum(),
                            gamer3Dice.getSum())

print(f'1등: {sortedNumbers[0]}, Winner')
print(f'2등: {sortedNumbers[1]}')
print(f'3등: {sortedNumbers[2]}')
# gamer1: [3, 1, 1, 4, 1]
# gamer2: [4, 6, 3, 6, 5]
# gamer3: [6, 2, 4, 2, 6]
# sum of gamer1: 10
# sum of gamer2: 24
# sum of gamer3: 20
# 1등: 24, Winner
# 2등: 20
# 3등: 10
