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
flag = True

members = {}

def access():
    members[userId] = userPw

def loginSuccess():
    print('로그인 성공')

def loginFail():
    print('로그인 실패')

def targetSearchSuccess():
    print(f'{targetId}: 회원정보 조회 성공')

def targetSearchFail():
    print(f'{targetId}: 회원정보 조회 실패')

def printUserInfo():
    print(f'회원ID: {members[userId]}, 회원PW: {userPw}, 회원Email: {userEmail}, 회원Phone: {userPhone}')

def reverseFlag():
    flag = False

def programOff():
    print('프로그램 종료')



while flag:
    selectedMenuNum = int(input(f'메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   99.종료'))

    if selectedMenuNum == 1:
        userId = input('ID 입력: ')
        userPw = input('PW 입력: ')
        userEmail = input('Email 입력: ')
        userPhone = input('Phone 입력: ')
        access()


    elif selectedMenuNum == 2:
        loginId = input('로그인ID 입력: ')
        loginPw = input('로그인PW 입력: ')

        if loginId in members:
            if members[userId] == userPw:
                if loginPw == userPw:
                    loginSuccess()

        else:
            reverseFlag()
            loginFail()
            

    elif selectedMenuNum == 3:
        targetId = input('회원ID 입력: ')
        targetPw = input('회원PW 입력: ')

        if targetId in members:
            if members[userId] == userPw:
                if targetPw == userPw:
                    targetSearchSuccess()
                    printUserInfo()
                
        else:
            reverseFlag()
            targetSearchFail()
        
    elif selectedMenuNum == 4:
        targetSearchSuccess()

    elif selectedMenuNum == 99:
        programOff()
        reverseFlag()



