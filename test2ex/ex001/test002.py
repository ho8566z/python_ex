'''
cm = float(input('원하는 길이를 입력하세요. '))
inch = .39 * cm

print(f'입력하신 {cm}cm는 {inch:.2f}inch입니다. ')
'''

'''
driveSpeed = int(input('당신의 속도를 입력하세요. '))
driveTime = float(input('당신의 주행시간을 입력하세요. '))
driveDistance = driveSpeed * driveTime

print(f'당신이 주행한 거리는 {driveDistance:.2f}km입니다. ')
'''

'''
import random
driveSpeed = random.randint(0, 130)
speedLimit = 80

if driveSpeed > 100:
    print(f'당신은 현재 {driveSpeed}km/h로 제한속도인 {speedLimit}보다 빠르게 [과속]하고 있습니다. ')
else:
    print(f'당신은 현재 {driveSpeed}km/h로 제한속도인 {speedLimit}보다 느리거나 같습니다. ')
'''

'''
num = int(input('원하는 정수를 입력하세요. '))

if num % 2 == 0:
    print(f'입력하신 {num}은 짝수입니다. ')
else:
    print(f'입력하신 {num}은 홀수입니다. ')
'''

'''
person = int(input('가구원의 수를 입력하세요 '))
print(f'당신의 가구원 수는 {person}입니다. ')

if person == 1:
    print(f'{person}인 가구의 국가재난지원금은 400,000원 입니다. ')
elif person == 2:
    print(f'{person}인 가구의 국가재난지원금은 600,000원 입니다. ')
elif person == 3:
    print(f'{person}인 가구의 국가재난지원금은 800,000원 입니다. ')
else:
    print(f'{person}인 가구의 국가재난지원금은 1,000,000원 입니다. ')
'''

'''
myScore = float(input('당신의 점수를 입력하세요. '))
print(f'당신의 점수는 {myScore}입니다. ')

if myScore >= 90:
    print('당신의 학점은 A입니다. ')
elif myScore >= 80:
    print('당신의 학점은 B입니다. ')
elif myScore >= 70:
    print('당신의 학점은 C입니다. ')
else:
    print('당신의 학점은 F입니다. ')
'''

''''''
tsetScore = float(input('당신의 점수를 입력하세요. '))
scoreLimit = 90

result = 'pass' if tsetScore >= scoreLimit else 'non pass'
print(f'테스트 결과: {result} ')

