# addList = ['A', 'B', 'C', 'D', 'E', 'F']
# print(addList)      #['A', 'B', 'C', 'D', 'E', 'F']
# print(addList[0])   #A

# print(f'addList: {addList}')    #addList: ['A', 'B', 'C', 'D', 'E', 'F']
# print(f'addList: {type(addList)}')   #addList: <class 'list'> -> 해당하는 속성: list

# print(addList[6])   #IndexError: list index out of range


# allList = [1, 1.1, 'A', 'And']
# print(allList)  #[1, 1.1, 'A', 'And']
# print(f'allList: {type(allList)}')  #allList: <class 'list'>


# addList = ['A', 'B', 'C', 'D', 'E', 'F']
# print(f'addList: {addList}')    #addList: ['A', 'B', 'C', 'D', 'E', 'F']
# print(F'addList length: {len(addList)}')    #addList length: 6

# print(f'1st data: {addList[0]}')    #1st data: A
# print(f'final data: {addList[len(addList)-1]}')    #final data: F


# wordList = "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle."
# print(f'wordList: {len(wordList)}')   #wordList: 110


# nameList = ['lando', 'max', 'gabriel','isack', 'pierre']
# print(f'{nameList[0]}')    # lando
# print(f'{nameList[1]}')    # max
# print(f'{nameList[2]}')    # gabriel
# print(f'{nameList[3]}')    # isack
# print(f'{nameList[4]}')    # pierre

# for name in nameList:
#     print(f'name: {name}')
# # name: lando
# # name: max
# # name: gabriel
# # name: isack
# # name: pierre

# nameIndex = 0
# for name in nameList:
#     print(f'name: {name}, nameIndex: {nameIndex}')
#     nameIndex += 1
# name: lando, nameIndex: 0
# name: max, nameIndex: 1
# name: gabriel, nameIndex: 2
# name: isack, nameIndex: 3
# name: pierre, nameIndex: 4

# for nameIndex, name in enumerate(nameList):
#     print(f'name: {name}, nameIndex: {nameIndex}')
# name: lando, nameIndex: 0
# name: max, nameIndex: 1
# name: gabriel, nameIndex: 2
# name: isack, nameIndex: 3
# name: pierre, nameIndex: 4

# while nameIndex < len(nameList):
#     print(f'{nameList[nameIndex]}, index: {nameIndex}')
#     nameIndex += 1
# lando, index: 0
# max, index: 1
# gabriel, index: 2
# isack, index: 3
# pierre, index: 4


# grandprixList = ['austraila', 'china', 'bahrain', 'saudiarabia', 'maimi']
# grandprixList.insert(2, 'japan')
# print(f'grandprixList: {grandprixList}')
#grandprixList: ['austraila', 'china', 'japan', 'bahrain', 'saudiarabia', 'maimi']


# spelling = ['A', 'B', 'C', 'D', 'F', 'G']
# spelling.insert(4, 'E')
# spelling.append('H')
# print(f'spelling: {spelling}')
# #spelling: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


# numList1 = [1, 2, 3, 4, 5]
# numList2 = [11, 12, 13, 14, 15]
# numList1.extend(numList1)
# print(f'numList1: {numList1}')  #numList1: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# numList1.extend(numList2)
# print(f'numList1: {numList1}')  #numList1: [1, 2, 3, 4, 5, 11, 12, 13, 14, 15]


# grandprixList = ['austraila', 'china', 'japan', 'bahrain', 'saudiarabia', 'maimi']
# grandprixList.pop()
# print(grandprixList)
# #['austraila', 'china', 'japan', 'bahrain', 'saudiarabia']

# grandprixList.pop(3)
# grandprixList.pop(4)
# print(grandprixList)
# #['austraila', 'china', 'japan', 'saudiarabia']

# removeGrandprix = grandprixList.pop()
# print(f'grandprixList: {grandprixList}')
# #grandprixList: ['austraila', 'china', 'japan', 'bahrain', 'saudiarabia']
# #grandprixList에서 마지막 데이터인 'maimi'가 삭제됨

# del grandprixList[3]
# del grandprixList[4]
# print(grandprixList)    #['austraila', 'china', 'japan', 'saudiarabia']


#-----------------------------------------------------------------------------------
print('-----------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------


# # quiz - 다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램
# sports  = ['baseball', 'basketball', 'tennis', 'golf', 'football']
# for idx1, idx2 in enumerate(sports):
#     if idx2 == 'football':
#         print(f'sports idx: {idx1}')    #sports idx: 4


# # quiz - 다음 리스트에서 'python' 문자열의 인덱스 값을 출력
# language = ['c/c++', 'c#', 'python', 'java']
# for idx, str in enumerate(language):
#     if str == 'python':
#         print(f'python idx: {idx}')     #python idx: 2


# quiz - 취미 추가하기
'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가되는 프로그램
그리고 취미의 개수 출력까지
'''
# hobbies = []
# flag = True

# while flag:
#     hobby = input(f'취미 추가: ')
#     hobbies.append(hobby)
#     print(f'hobbies: {hobbies}')
#     plus = int(input(f'1.계속  2.종료'))
#     if plus == 2:
#         flag = False


# quiz - 누락된 숫자 추가하기
# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers 리스트를 보고 1~10까지 숫자 중 누락된 숫자를 추가

# numbers = [1, 2, 3, 4, 5, 7, 8, 9]
# numbers.insert(5, 6)
# numbers.append(10)
# print(f'numbers: {numbers}')    #numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# #quiz - sports 리스트에서 'tennis'을 삭제하는 프로그램
# sports = ['baseball', 'basketball', 'tennis', 'football']
# sports.remove('tennis')
# print(f'sports: {sports}')    #sports: ['baseball', 'basketball', 'football']

# #quiz - sports 리스트에서 'tennis'을 삭제하는 프로그램
# sports = ['baseball', 'basketball', 'tennis', 'football']
# tennisIndex = sports.index('tennis')
# sports.pop(tennisIndex)
# print(f'sports: {sports}')    #sports: ['baseball', 'basketball', 'football']
# print(f'tennisIndex: {tennisIndex}')    #tennisIndex: 2

