# 데이타 입력(input data)
# input()

'''
print('데이터를 입력하세요.')
inputData = input()
print(inputData)
'''

'''
print('정수를 입력하세요.')
inputInteger = input()
print(inputInteger)
print(type(inputInteger))
'''

'''
print('실수를 입력하세요.')
inputFloat = input()
print(inputFloat)
print(type(inputFloat))
'''

'''
print('논리형 데이터를 입력하세요.')
inputBoolean = input()
print(inputBoolean)
print(type(inputBoolean))
'''

'''
inputBoolean = input('논리형 데이터를 입력하세요.\n')
print(inputBoolean)
print(type(inputBoolean))
'''

'''
print('논리형 데이터를 입력하세요.', end='')
inputBoolean = input()
print(inputBoolean)
print(type(inputBoolean))

inputBoolean = input('논리형 데이터를 입력하세요.', end='')
print(inputBoolean)
print(type(inputBoolean))
'''


'''
userInputData = input('정수 입력하시오')
print(userInputData)
print(type(userInputData))
int(userInputData) #userInputData라는 데이터 원본을 변형시키는게 아닌, 데이터를 복사하고, 이것을 변형하는 명령
print(type(userInputData)) #때문에 다시 출력해도 'str'문자열로 출력된다

userInputData = input('정수 입력하시오')
print(userInputData)
print(type(userInputData))
userInputData = int(userInputData)
print(type(userInputData))
'''


# userInputData = input('True or False 입력하세요.')
# print(userInputData) #True
# print(type(userInputData)) #str
# userInputData = bool(userInputData)
# print(type(userInputData))


# userInputData = input('실수를 입력하세요.')
# print(userInputData)
# print(type(userInputData))
# userInputData = float(userInputData)
# print(type(userInputData))


# x = 3
# y = float(x)
# print(y)
# print(type(y)) #3인 int데이터를 float로 변경시키면서 뒤에 '.0'이 붙으면서 데이터가 변형됨

# x = 3.14
# y = int(x)
# print(y)
# print(type(y)) #3.14인 float데이터를 int로 변경시키면서 뒤에'.14'는 날라감

