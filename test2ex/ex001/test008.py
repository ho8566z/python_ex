# # Toy 프로젝트
# '''
# 처음 프로그램이 실행하면, 다음과 같은 메뉴를 출력한다
# 메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   99.종료
# '1.회원가입'을 선택하면, 회원ID, 회원Email, 회원Phone 정보를 입력받아 회원가입을 진행한다
# '2.로그인'을 선택하면, 회원ID, 회원PW를 입력받아 로그인 '성공'또는 '실패'를 출력한다
# '3.특정 회원정보 출력'을 선택하면, 회원ID와 회원PW를 입력받아 일치하는 회원정보를 모두 출력한다
# '4.모든 회원정보 출력'을 선택하면, 가입되어있는 모든 회원정보를 출력한다
# '99.종료'를 선택하면, 프로그램을 종료한다

# 이후에, 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원정보를 수정하는 기능을 구현할 것
# '''
# flag = True

# members = {}

# def access(userId, userPw, userEmail, userPhone):
#     members[userId] = {
#         'pw': userPw,
#         'email': userEmail,
#         'phone': userPhone
#     }

# def accessSuccess():
#     print('회원가입 성공')

# def loginSuccess():
#     print('로그인 성공')

# def loginFail():
#     print('로그인 실패')

# def targetSearchSuccess(targetId):
#     print(f'{targetId}: 회원정보 조회 성공')

# def targetSearchFail(targetId):
#     print(f'{targetId}: 회원정보 조회 실패')

# def printUserInfo(userId):
#     info = members[userId]
#     print("="*50)
#     print(f'회원ID: {userId}, 회원PW: {info['pw']}, 회원Email: {info['email']}, 회원Phone: {info['phone']}')
#     print("="*50) 

# def printAllInfo():
#     if not members:
#         print('미가입 회원입니다.')
#         return

#     print("="*50)
#     print('전체 회원 목록')
#     for userId, info in members.items():
#         print(f'ID: {userId}, Email: {info['email']}, Phone: {info['phone']}')
#     print("="*50)

# def editSuccess():
#     print(f'[{editId}] 인증성공, 새로운 회원정보를 입력하세요.')
#     members[editId]['pw'] = input('새로운 회원PW 입력: ')
#     members[editId]['email'] = input('새로운 회원Email 입력: ')
#     members[editId]['phone'] = input('새로운 회원Phone 입력: ')
#     print('회원정보 수정이 완료되었습니다.')

# def editFil():
#     print('인증 실패, 회원정보가 일치하지 않습니다.')

# while flag:
#     print("="*50)
#     selectedMenuNum = int(input(f'메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   5.회원정보 수정   99.종료'))
#     print("="*50)

#     if selectedMenuNum == 1:
#         userId = input('ID 입력: ')
#         if userId in members:
#             print('중복 ID입니다.')
#             continue
#         userPw = input('PW 입력: ')
#         userEmail = input('Email 입력: ')
#         userPhone = input('Phone 입력: ')
#         access(userId, userPw, userEmail, userPhone)
#         accessSuccess()


#     elif selectedMenuNum == 2:
#         loginId = input('로그인ID 입력: ')
#         loginPw = input('로그인PW 입력: ')

#         if loginId in members and members[loginId]['pw'] == loginPw:
#             loginSuccess()

#         else:
#             loginFail()
            

#     elif selectedMenuNum == 3:
#         targetId = input('회원ID 입력: ')
#         targetPw = input('회원PW 입력: ')

#         if targetId in members and members[targetId]['pw'] == targetPw:
#             targetSearchSuccess(targetId)
#             printUserInfo(targetId)
                
#         else:
#             targetSearchFail(targetId)
        
#     elif selectedMenuNum == 4:
#         printAllInfo()

#     elif selectedMenuNum == 5:
#         editId = input('수정할 회원ID 입력: ')
#         editPw = input('회원PW 입력: ')

#         if editId in members and members[editId]['pw'] == editPw:
#             editSuccess()
        
#         else:
#             editFil()

#     elif selectedMenuNum == 99:
#         print('프로그램을 종료합니다.')
#         flag = False

#     else:
#         print('메뉴를 다시 선택해주세요.')



#----------------------------------------------------------------------
#----------------------------2회차: clone코딩----------------------------
#----------------------------------------------------------------------

# Toy 프로젝트
'''
처음 프로그램이 실행하면, 다음과 같은 메뉴를 출력한다
메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   99.종료
'1.회원가입'을 선택하면, 회원ID, 회원Email, 회원Phone 정보를 입력받아 회원가입을 진행한다
'2.로그인'을 선택하면, 회원ID, 회원PW를 입력받아 로그인 '성공'또는 '실패'를 출력한다
'3.특정 회원정보 출력'을 선택하면, 회원ID와 회원PW를 입력받아 일치하는 회원정보를 모두 출력한다
'4.모든 회원정보 출력'을 선택하면, 가입되어있는 모든 회원정보를 출력한다
'99.종료'를 선택하면, 프로그램을 종료한다

이후에, 특정 회원의 회원ID와 회원PW를 입력받아 인증되면 회원정보를 수정하는 기능을 구현할 것
'''

members = {}

def addMember(uId, uPw, uEmail, uPhone):
    members[uId] = {
        'pw': uPw, 
        'email': uEmail,
        'phone': uPhone
    }

def existId(uId):
    return uId in members

def authenticate(uId, uPw):
    if existId and members[uId]['pw'] == uPw:
        return True
    return False

def getMember(uId):
    return members[uId]

def getAllMember():
    return members

def updateMember(uId, uEmail, uPhone):
    members[uId]['email'] = newEmail
    members[uId]['phone'] = newPhone


def runRegister():
    print('----- 회원가입 -----')
    uId = input('신규회원 ID 입력: ')
    if existId(uId):
        print('중복 ID입니다.')
        return
    
    uPw = input('신규회원 PW: ')
    uEmail = input('신규회원 Email: ')
    uPhone = input('신규회원 Phone: ')

    addMember(uId, uPw, uEmail, uPhone)
    print('회원가입 성공')

def runLogin():
    print('----- 로그인 -----')
    uId = input('로그인 ID: ')
    uPw = input('로그인 PW: ')

    if authenticate(uId, uPw):
        print('로그인 성공')
    else:
        print('로그인 실패')

def runPrintMember():
    print('----- 특정 회원정보 출력 -----')
    uId = input('조회 ID: ')
    uPw = input('조회 Pw: ')

    if authenticate(uId, uPw):
        info = getMember(uId)
        print(f'[조회결과] ID: {uId}, Email: {info['email']}, Phone: {info['phone']}')
    else:
        print('인증 실패')

