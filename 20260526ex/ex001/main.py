import lotto_ex as lm

nums = []

print('1부터 45까지의 정수 6개를 입력하세요.')
nums.append(int(input('첫번째 숫자 입력: ')))
nums.append(int(input('두번째 숫자 입력: ')))
nums.append(int(input('세번째 숫자 입력: ')))
nums.append(int(input('네번째 숫자 입력: ')))
nums.append(int(input('다섯번째 숫자 입력: ')))
nums.append(int(input('여섯번째 숫자 입력: ')))

lm.setUNumbers(nums)    #사용자가 선책한 번호모음
lm.setRNumbers()        #랜덤으로 선택한 번호모음

print(f'이번주 로또 번호: {lm.getRNumbers()}')
print(f'내가 선택한 로또 번호: {lm.getUNumbers()}')
print(f'일치하는 로또 번호: {lm.compareNumbers()}')
# 1부터 45까지의 정수 6개를 입력하세요.
# 첫번째 숫자 입력: 1
# 두번째 숫자 입력: 3
# 세번째 숫자 입력: 12
# 네번째 숫자 입력: 16
# 다섯번째 숫자 입력: 33
# 여섯번째 숫자 입력: 43
# 이번주 로또 번호: [9, 36, 19, 6, 41, 30]
# 내가 선택한 로또 번호: [1, 3, 12, 16, 33, 43]
# 일치하는 로또 번호: []

