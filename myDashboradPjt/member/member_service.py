from util import util_time
from member import config as member_config
import config as root_config
import os
import json
import session

class MemberSerive:
    def __init__(self):
        self.members = {}
        self.init_database()

    # 회원 가입 기능
    def sign_up(self):
        mId = input('Input new member ID: ')

        # ID 중복체크를 할 때 self.members를 사용한다.
        if mId in self.members:
            print('이미 사용중인 ID 입니다.')
            return

        mPw = input('Input new member PW: ')
        mMail = input('Input new member MAIL: ')
        mPhone = input('Input new member PHONE: ')

        newMember = {
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone,
            'mRegDate': util_time.getCurrentDateTime(),
            'mModDate': util_time.getCurrentDateTime(),
        }

        self.members[mId] = newMember

        # DB(members.json)에 새 회원 정보 저장
        self.save_members(self.members)  # {}

        print('MEMBER SIGN-UP SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 로그인 기능
    def sign_in(self):
        mId = input('Input member ID: ')
        mPw = input('Input member PW: ')

        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('MEMBER SIGN-IN SUCCESS!!')

#================================================================================================#

            # session.signInedMemberId = mId
            session.setSignInedMemberId(mId)
        #데이터 무결성: 데이터는 어느때라도, 지켜야하기 때문에
        #-> 함수를 통해 데이터를 간접적으로 다루는게 이상적이고, 
        # 데이터 원본을 최소한이라도 보호하는 것이다
        #(함수와 클래스가 데이터 제어권을 가지며, 유효성 검사를 진행하고, 
        # 차등적인 데이터 접근권한을 검증한다)

#================================================================================================#

            if root_config.DEV_MOD:
                print(f'session.signInedMemberId: {session.signInedMemberId}')
        else:
            print('MEMBER SIGN-IN FAIL!!')

        # #바로 위의 코드와 기능적으로 같음(현업에서 많이 사용됨)
        # self.members = self.loadMembers()
        # if mId in self.members and self.members[mId]['mPw'] == mPw:
        #     print('MEMBER SIGN-IN : SUCCESS')
        #     return
        # print('MEMBER SIGN-IN : FAIL')

#================================================================================================#

    # 회원 로그아웃 기능
    def sign_out(self):
        session.setSignInedMemberId()
        print('SIGN-OUT SUCCESS!!')

    # 회원 정보수정 기능
    def modify(self):
        mPw = input('Input member PW: ')
        mMail = input('Input member MAIL: ')
        mPhone = input('Input member PHONE: ')

        self.members = self.load_members()
        memberForModify = self.members[session.getSignInedMemberId()]

        memberForModify['mPw'] = mPw
        memberForModify['mMail'] = mMail
        memberForModify['mPhone'] = mPhone
        memberForModify['mModDate'] = util_time.getCurrentDateTime()

        self.save_members(self.members)

        print(f'MODIFY SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 탈퇴 기능
    def delete(self):
        confirm = input('정말 탈퇴하시겠습니까? [Y] or [N]')
        if confirm == 'Y':
            self.members = self.load_members()
            del self.members[session.getSignInedMemberId()]
            self.save_members(self.members)
            session.setSignInedMemberId()
            print('DELETE SUCCESS!!')

            if root_config.DEV_MOD:
                print(f'self.load_members(): {self.load_members()}')

    def run(self):
        flag = True
        # while flag:
        while flag:
            # if session.signInedMemberId == '':
            if session.getSignInedMemberId() == '':
                menuNum = int(input('1.SIGN-UP    2.SIGN-IN    99.SERVICE-OUT '))
            else:
                menuNum = int(input('3.SIGN-OUT    4.MODIFY    5.DELETE    99.SERVICE-OUT '))
            
            if menuNum == member_config.SIGN_UP:
                self.sign_up()
            elif menuNum == member_config.SIGN_IN:
                self.sign_in()
            elif menuNum == member_config.SIGN_OUT:
                self.sign_out()
            elif menuNum == member_config.MODIFY:
                self.modify()
            elif menuNum == member_config.DELETE:
                self.delete()
            elif menuNum == member_config.SERVICE_OUT:
                flag = False

    def init_database(self):
        
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')
        #C:\lyh\python\python_ex\myDashboardPjt\member 

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')
        #C:\lyh\python\python_ex\myDashboardPjt

        # db/members.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\lyh\python\python_ex\myDashboardPjt\db\members.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_members(self.members)
        else:
            self.members = self.load_members()

    # JSON 파일 저장
    def save_members(self, members):   # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

    def load_members(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

if __name__ == '__main__':
    memberSerive = MemberSerive()
    memberSerive.run()