# # Toy 프로젝트
# '''
# 처음 프로그램이 실행하면, 다음과 같은 메뉴를 출력한다
# 메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   99.종료

# '1.회원가입'을 선택하면, 회원ID, 회원Email, 회원Phone 정보를 입력받아 회원가입을 진행한다
# '2.로그인'을 선택하면, 회원ID, 회원PW를 입력받아 로그인 '성공'또는 '실패'를 출력한다
# --> 인증(Authentication), 인가(authorization)
# '3.특정 회원정보 출력'을 선택하면, 회원ID와 회원PW를 입력받아 일치하는 회원정보를 모두 출력한다
# '4.모든 회원정보 출력'을 선택하면, 가입되어있는 모든 회원정보를 출력한다
# '99.종료'를 선택하면, 프로그램을 종료한다
# '''

# SIGN_UP             = 1
# SIGN_IN             = 2
# PRINT_MY_INFO       = 3
# PRINT_ALL_MEMBER_INFO      = 4
# SYSTEM_SHUTDOWN     = 99

# DEV_MOD = False

# members = {}

# if DEV_MOD:

#     uIds = ['1111', '5555', 'aaaa']
#     uPws = ['2222', '6666', 'bbbb']
#     uEmails = ['3333', '7777', 'cccc']
#     uPhones = ['4444', '8888', 'dddd']

#     for n in range(len(uIds)):
#         members[uIds[n]] = {
#             'uId': uIds[n],
#             'uPw': uPws[n],
#             'uEmail': uEmails[n],
#             'uPhone': uPhones[n]
#         }

# # functions START
# def getSelectedMenuNum():
#     selectedMenuNum = int(input('메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료'))
#     return selectedMenuNum

# def setNewNum(uId, uPw, uEmail, uPhone):
#     members[uId] = {
#         'uId': uId,
#         'uPw': uPw,
#         'uEmil': uEmail,
#         'uPhone': uPhone
#     }

# def isMember(uId):
#     if uId in members:
#         print(f'{uId}은/는 이미 사용중입니다. 다시 입력하세요.')
#         return True
#     else:
#         return False

# def printAllMemberInfo(value):
#     for key1, value1 in value.items():
#         print(f'{key1}: {value1}')

# # function END


# flag = True
# while flag:
    
#     userSelectedMenuNum = getSelectedMenuNum()

#     if userSelectedMenuNum == SIGN_UP:        #1.회원가입
#         uId = input('input member ID: ')
#         if not isMember(uId):       #False: 회원이 없는 경우(가입o), True: 회원이 있는 경우(가입x)
#             uPw = input('input membetr PW: ')
#             uEmail = input('input member Email: ')
#             while True:
#                 if '@' not in uEmail:
#                     print('입력한 Email주소가 형식에 맞지 않습니다.')
#                     uEmail = input('input member Email: ')
#                 else:
#                     break

#         uPhone = input('input membetr Phone: ')

#         setNewNum(uId, uPw, uEmail, uPhone)
#         # members[uId] = {
#         #         'uId': uId,
#         #         'uPW': uPw,
#         #         'uEmil': uEmail,
#         #         'uPhone': uPhone
#         #     }

#         print('SIGN UP - SUCCESS')

#         if DEV_MOD: print(f'members: {members}')


#     elif userSelectedMenuNum == SIGN_IN:      #2.로그인
#         signInCount = 0
#         while True:
#             uId = input('input member ID: ')
#             uPw = input('input member PW: ')

#             if uId in members:
#                 uInfo = members[uId]
#                 if uInfo['uPw'] == uPw:
#                     print('SIGN UP - SUCCESS')
#                     break
#                 else:
#                     print('SIGN UP - FAIL')
#                     signInCount += 1
#                     if signInCount >= 3:
#                         print('로그인을 3회 실패했습니다.')
#                         break
#             else:
#                 print(f'존재하지 않는 ID입니다.')
#                 signInCount += 1
#                 if signInCount >= 3:
#                     print('로그인을 3회 실패했습니다.')
#                     break


#     elif userSelectedMenuNum == PRINT_MY_INFO:      #3.내 회원정보 출력
#         uId = input('input member ID: ')
#         uPw = input('input membetr PW: ')

#         if uId in members:
#             uInfo = members[uId]
#             if uInfo['uPw'] == uPw:
#                 print('SIGN UP - SUCCESS')

#                 print('-' * 40)
#                 for key, value in uInfo.items():
#                     print(f'{key}: {value}')
#                 print('-' * 40)

#             else:
#                 print('SIGN UP - FAIL')
#         else:
#             print(f'존재하지 않는 ID입니다.')

#     elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:      #4.모든 회원정보 출력
#         for key, value in members.items():
#             print(f'{key}님의 정보---------------------------')
#             printAllMemberInfo(value)
#             print('-' * 40)

#     elif userSelectedMenuNum == SYSTEM_SHUTDOWN:     #99.종료
#         flag = False
#         print('Good Bye')
# # 메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료1
# # input member ID: 1111
# # input membetr PW: 2222
# # input member Email: 3333@
# # input membetr Phone: 4444
# # SIGN UP - SUCCESS
# # 메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료2
# # input member ID: 1111
# # input member PW: 2222
# # SIGN UP - SUCCESS
# # 메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료3
# # input member ID: 1111
# # input membetr PW: 2222
# # SIGN UP - SUCCESS
# # ----------------------------------------
# # uId: 1111
# # uPw: 2222
# # uEmil: 3333@
# # uPhone: 4444
# # ----------------------------------------
# # 메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료4
# # 1111님의 정보---------------------------
# # uId: 1111
# # uPw: 2222
# # uEmil: 3333@
# # uPhone: 4444
# # ----------------------------------------
# # 메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료99
# # Good Bye

