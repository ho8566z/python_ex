from db import dbManager
from memberService import session
from bankAccount import bankAccount


def isExistsId(id):
    return id in dbManager.getMemberIds()


def isValidAccount(id, pw):
    if isExistsId(id):
        if pw == dbManager.getMemberPw(id):
            return True


def signUp():
    id = input("아이디: ")

    if isExistsId(id):
        print("중복된 아이디입니다.")
        return

    pw = input("패스워드: ")
    mail = input("이메일: ")
    phone = input("전화번호: ")

    dbManager.createMember(id, pw, mail, phone)
    #모듈: dbManager의 create(만든다), member(회원을)에서 
    # 'id, pw, mail, phone을 매개변수로서' 데이터를 가져온다
    bankAcnt = bankAccount.setBankAccount(id)
    #변수명: '은행 계좌'는 모듈: bankAccount의 
    # 함수: set(설정)힌다, bank(은행)의 account(계좌)를 
    # = 은행계좌를 설정히는 함수를 'id'를 매개변수로서 데이터를 할당한다

    #다른 데이터들과 달리 '은행계좌'는 사용자로부터 input받지 않고, 
    # 고정 계좌번호 '101-77-'에 사용자의 'id'를 더해 만들어지기 때문에
    # 회원정보 중에 가장 늦게 키값과 밸류값 쌍을 이루게 된다
    #ex) '101-77-[id]'

    print("회원가입에 성공했습니다.")


def signIn():
    id = input("아이디: ")
    pw = input("패스워드: ")

    if not isValidAccount(id, pw):
        print("로그인에 실패했습니다.")
        return

    print("로그인 성공.")
    session.signinedId = id


def signOut():
    print("로그아웃 완료.")
    session.signinedId = ""
