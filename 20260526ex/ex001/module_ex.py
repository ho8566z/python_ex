# 자주 사용하는 모듈: 내장 모듈
# 이러한 내장 모듈은 절대로 외우는 것이 아니고, 가볍게 훑고 필요할 때, 찾아서 사용하면 됨

# math 모듈: 수학과 관련된 모듈
'''
fabs(): 절댓값을 반환
ceil(): 소수점 이하 올림한 값을 반환
floor(): 소수점 이하 내림한 값을 반환
trunc(): 소수점 이하 버림한 값을 반환
gcd(): 최대공약수를 반환'
factorial(): 팩토리얼한 값을 반환
sqrt(): 제곱근을 반환
'''

import math

print(f'math.fabs(-3.1415): {math.fabs(-3.1415)}')      # 절댓값
print(f'math.ceil(3.1415): {math.ceil(3.1415)}')        # 올림
print(f'math.floor(-3.1415): {math.floor(-3.1415)}')    # 내림
print(f'math.trunc(-3.1415): {math.trunc(-3.1415)}')    # 버림
print(f'math.gcd(9, 21): {math.gcd(9, 21)}')            # 절댓값
print(f'math.factorial(7): {math.factorial(7)}')        # 팩토리얼
print(f'math.sqrt(9): {math.sqrt(9)}')                  # 제곱근
# math.fabs(-3.1415): 3.1415
# math.ceil(3.1415): 4
# math.floor(-3.1415): -4
# math.trunc(-3.1415): -3
# math.gcd(9, 21): 3
# math.factorial(7): 5040
# math.sqrt(9): 3.0


# 파이썬 내장 함수 중에서 수학과 관련된 함수
'''
sum(): 전체값을 반환
max(): 최댓값을 반환
min(): 최솟값을 반환
abs(): 절댓값을 반환
pow(): 거듭제곱을 반환
round(): 반올림한 값을 반환
'''


# random 모듈: 난수를 발생시키는 모듈
'''
random(): 0이상 1미만의 난수 발생
randint(n1, n2): n1이상 n2이하의 난수 발생
randrange(n1, n2): n1이상 n2미만의 난수 발생
sample(range(n1, n2), n3): n1이상 n2미만의 난수 n3개 발생(중복없이)
choice(): 무작위 1개 아이템 선택
shuffle(): 아이템 순서 섞음
'''

import random

print(f'random(): {random.random()}')                   # 0이상 1미만 난수
print(f'random(): {random.randint(0, 9)}')              # 0이상 9이하 난수
print(f'random(): {random.randrange(0, 9)}')            # 0이상 9미만 난수
print(f'random(): {random.sample(range(0, 10), 3)}')    # 0이상 10미만 난수 3개


listVar = [1, 2, 3, 4, 5, 6]

# 무작위로 1개 아이템 선택
print(f'choice: {random.choice(listVar)}')
print(f'choice: {random.choice(listVar)}')


# 아이템 순서 섞음
random.shuffle(listVar)
print(f'listVar: {listVar}')    #listVar: [4, 1, 6, 5, 2, 3]
random.shuffle(listVar)
print(f'listVar: {listVar}')    #listVar: [3, 4, 2, 1, 6, 5]


# time 모듈: 시간 관련 모듈(UTC)
'''
localtime(): 시스템의 현재 시간을 반환
gmtime(): GMT 시간을 반환
strftime(): 시간 포맷 코드에 따른 출력
'''

import time

lt = time.localtime()       # 시스템 시간
print(f'lt: {lt}')
# lt: time.struct_time(tm_year=2026, tm_mon=5, tm_mday=26, tm_hour=9, 
# tm_min=49, tm_sec=39, tm_wday=1, tm_yday=146, tm_isdst=0)

print(f'년 일: {lt.tm_yday}')   # 년 일: 146
print(f'년도: {lt.tm_year}')    # 년도: 2026
print(f'월: {lt.tm_mon}')       # 월: 5

week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

print(f'요일: {week[lt.tm_wday]}')    # 요일: 화요일

'''
0: 월요일
1: 화요일
2: 수요일
3: 목요일
4: 금요일
5: 토요일
6: 일요일
'''


gt = time.gmtime()      #GMT 시간: 그리니치 천문대 기준 시간

print(F'gt: {gt}')
# gt: time.struct_time(tm_year=2026, tm_mon=5, tm_mday=26, tm_hour=0, 
# tm_min=49, tm_sec=39, tm_wday=1, tm_yday=146, tm_isdst=0)

print(F'gt.tm_hour: {gt.tm_hour}')      # gt.tm_hour: 0(그리니치 기준: 0시)


print(f'시:분:초: {time.strftime('%H:%M:%S', time.localtime())}')       #시:분:초: 10:02:56
print(f'연:월:일 시:분:초: {time.strftime('%Y:%m:%d %H:%M:%S', time.localtime())}')
# 연:월:일 시:분:초: 2026:05:26 10:04:32



# quiz - lotto game
# 20260526ex --> ex001 --> lotto_ex.py
