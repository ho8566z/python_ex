from config_dir.dir import config
from member import session
from db import member_db
from db import diary_db
from member import member_dumy
import copy

if config.DEV_MOD:
    member_dumy.dumyInit()
    print(f'memberDB: {member_db.memberDB}')

flag = True

while flag:

    menuNum = ''
    if session.signInedMemberid == '':
        # sign-out 일때
        menuNum = int(input('1.sign-up | 2.sign-in | 6.write | 7.read | 99.end'))
    else:
        # sign-in 일때
        menuNum = int(input('3.modify | 5.sign-out | 4.delete | 6.write | 7.read | 99.end'))


    if menuNum == config.SIGN_UP:
        print('1.sign-up')
        uId = input('please input new member ID: ')
        uPw = input('please input new member PW: ')
        uMail = input('please input new member MAIL: ')
        uPhone = input('please input new member PHONE: ')

        member_db.memberDB[uId] = {
            'uId': uId,
            'uPw': uPw,
            'uMail':uMail,
            'uPhone': uPhone
        }

        print('New member sign-up success')

        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')

        diary_db.diaryDB[uId] = []

    elif menuNum == config.SIGN_IN:
        print('2.sign-in')
        uId = input('please input member ID: ')
        uPw = input('please input member PW: ')


        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success')
                session.signInedMemberid = uId
            else:
                print('sign-in fail -- PW trouble')
        else:
            print('sign-in fail -- ID trouble')

        # if uId in member_db.memberDB and member_db.memberDB[uId]['uPw'] == uPw:
        #         print('sign-in success')
        # else:
        #     print('sign-in fail -- ID or PW trouble')


    elif menuNum == config.MEMBER_MODIFY:
        print('3.modify')
        '''
        id pw, mail, phone 중에서 어떤 정보들을 수정가능케 할지 정해야 한다
        id: x, 또한 이미 탈퇴한 사용자의 id라도 절대 변경/수정을 허용하는 것은 않된다
        pw: 절대 수정이 불가능하지는 않지만, 쉽게 변경할 수는 없다
        mail, phone: 비교적 수정이 간단하게 가능하다 
        '''
        uPw = input('please input member PW: ')
        uMail = input('please input member MAIL: ')
        uPhone = input('please input member PHONE: ')
        '''
            -member_db 모듈에 있는 memberDB 딕셔너리에서 회원정보를 변경한다
            -현재 member_db에는 'gildong', 'chanho'회원이 존재하기 때문에, 
            -현 상황에 로그인되어 있는 회원의 정보를 불러와서 회원정보를 수정한다
            -즉, session.signInedMemberid에 현재 로그인되어 있는 회원의 ID를 
                가져와서 사용하면 된다
        '''
        currentSignInedMemberID = session.signInedMemberid
        memberInfo = member_db.memberDB[currentSignInedMemberID]

        if config.DEV_MOD: print(f'memberInfo: {memberInfo}')

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        if config.DEV_MOD: print(f'after modify: memberInfo: {memberInfo}')

    elif menuNum == config.MEMBER_DELETE:
        print('4.delete')
        '''
        현재 로그인 되어 있는 회원의 id를 session.signInedMemberid에서 가져와서
        해당하는 회원의 정보를 member_db.memberDB에서 삭제한다
        '''
        currentSignInedMemberID = session.signInedMemberid
        del member_db.memberDB[currentSignInedMemberID]
        
        print('member info delete')
        session.signInedMemberid = ''

        if config.DEV_MOD: print(f'member_db.memberDB: {member_db.memberDB}')

    elif menuNum == config.SYSTEM_OUT:
        print('99.end')
        flag = False

    elif menuNum == config.SIGN_OUT:
        print('5.sign-out')
        '''
        메뉴를 변경한다
        로그인 값 또한 변경한다
        session모듈에 signinedMemverId 변수에 있는지?
        '''
        print('sign-out success')
        session.signInedMemberid = ''

    elif menuNum == config.DIARY_WRITE:
        print(f'6.write')

        if session.signInedMemberid == '':
            print('sorry, please sign-in')
        else:
            while True:
                diaryTxt = input('10자 이하의 짧은 글을 입력하세요. ')
                if len(diaryTxt) > 10:
                    print(f'10자를 초과했습니다.({len(diaryTxt)})')
                else:
                    diary_db.diaryDB[session.signInedMemberid].append(diaryTxt)
                    if config.DEV_MOD: print(f'diary_db.diaryDB: {diary_db.diaryDB}')
                    break

    elif menuNum == config.DIARY_READ:
        print(f'7.read')

        if session.signInedMemberid == '':
            print('sorry, please sign-in')
        else:
            currentSignInedMemberID = session.signInedMemberid
            myDiaries = diary_db.diaryDB[currentSignInedMemberID]

            deepcopiedDiaries = copy.deepcopy(myDiaries)
            deepcopiedDiaries.reverse()
            for idx, diaryTxt in enumerate(deepcopiedDiaries):
                print(f'({idx +1}): {diaryTxt}')

