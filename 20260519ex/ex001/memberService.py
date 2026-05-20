# Toy 프로젝트
'''
처음 프로그램이 실행하면, 다음과 같은 메뉴를 출력한다
메뉴: 1.회원가입   2.로그인   3.특정 회원정보 출력   4.모든 회원정보 출력   
5.회원정보 수정   99.종료

'1.회원가입'을 선택하면, 회원ID, 회원Email, 회원Phone 정보를 입력받아 회원가입을 진행한다
'2.로그인'을 선택하면, 회원ID, 회원PW를 입력받아 로그인 '성공'또는 '실패'를 출력한다
--> 인증(Authentication), 인가(authorization)
'3.특정 회원정보 출력'을 선택하면, 회원ID와 회원PW를 입력받아 일치하는 회원정보를 모두 출력한다
'4.모든 회원정보 출력'을 선택하면, 가입되어있는 모든 회원정보를 출력한다
'5.회원정보 수정'을 선택하면, 변경하려는 회원의 ID와 PW를 입력받아 인증하고, 회원정보를 수정한다
'99.종료'를 선택하면, 프로그램을 종료한다
'''

SIGN_UP             = 1
SIGN_IN             = 2
PRINT_MY_INFO       = 3
PRINT_ALL_INFO      = 4
SYSTEM_SHUTDOWN     = 99

DEV_MOD = True

members = {}

if DEV_MOD:
    members['1111'] = {
        'uId': '1111',
        'uPw': '2222',
        'uEmail': '3333',
        'uPhone': '4444'
    }


flag = True
while flag:
    selectedMenuNum = int(input('메뉴: 1.회원가입   2.로그인   3.내 회원정보 출력   4.모든 회원정보 출력   99.종료'))

    if selectedMenuNum == SIGN_UP:        #1.회원가입
        uId = input('input member ID: ')
        uPw = input('input membetr PW: ')
        uEmail = input('input member EMAIL: ')
        uPhone = input('input membetr PHONE: ')

        members[uId] = {
            'uId': uId,
            'uPW': uPw,
            'uEmil': uEmail,
            'uPhone': uPhone
        }

        print('SIGN UP - SUCCESS')

        if DEV_MOD: print(f'members: {members}')


    elif selectedMenuNum == SIGN_IN:      #2.로그인
        uId = input('input member ID: ')
        uPw = input('input membetr PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN UP - SUCCESS')
            else:
                print('SIGN UP - FAIL')
        else:
            print(f'존재하지 않는 ID입니다.')


    elif selectedMenuNum == PRINT_MY_INFO:      #3.내 회원정보 출력
        uId = input('input member ID: ')
        uPw = input('input membetr PW: ')

        if uId in members:
            uInfo = members[uId]
            if uInfo['uPw'] == uPw:
                print('SIGN UP - SUCCESS')

                print('-' * 40)
                for key, value in uInfo.items():
                    print(f'{key}: {value}')
                print('-' * 40)

            else:
                print('SIGN UP - FAIL')
        else:
            print(f'존재하지 않는 ID입니다.')

    elif selectedMenuNum == PRINT_ALL_INFO:      #4.모든 회원정보 출력
        pass

    elif selectedMenuNum == SYSTEM_SHUTDOWN:     #99.종료
        flag = False
        print('Good Bye')

