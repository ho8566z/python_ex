import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid
from util import util_time

class BankService:
    '''로그인한 회원의 계좌를 관리하고 accounts.json 에 저장하는 서비스 클래스.'''
    def __init__(self):
        self.accounts = {}
        self.init_database()


    def init_database(self):
        '''db/accounts.json 경로를 정하고, 파일이 없으면 새로 만들고 있으면 불러온다.'''
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/accounts.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'accounts.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\lyh\python\python_ex\myDashboardPjt\db\accounts.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_accounts(self.accounts)
        else:
            self.accounts = self.load_accounts()


    # JSON 파일 저장
    def save_accounts(self, accounts):   # {}
        '''계좌 딕셔너리를 JSON 파일에 저장한다. db 폴더가 없으면 만든다.'''
        os.makedirs(os.path.dirname(self.dbFile), exist_ok=True)
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)


    def load_accounts(self):
        '''JSON 파일에서 전체 계좌 정보를 읽어 딕셔너리로 반환한다.'''
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        

    def isMyAccount(self):
        '''로그인한 회원의 계좌가 하나라도 있는지 반환한다.'''
        allAcccounts = self.load_accounts()
        if session.getSignInedMemberId() in allAcccounts:
            return True
        
        return False


    def run(self):
        '''로그인 확인 후 계좌 목록·개설·입금·출금 메뉴를 반복 처리한다.'''

        if session.getSignInedMemberId() == '':
            print('Please SIGN-IN!!')
            return

        flag = True
        while flag:

            if self.isMyAccount():
                try:
                    menuNum = int(input('1.ACCOUNT-LIST    2.NEW-ACCOUNT    3.DEPOSIT    4.WITHDRAWAL    99.SERVICE-OUT :  '))
                except ValueError:
                    print('Please enter a valid menu number!!')
                    continue
            else:
                print('No account yet!!')
                try:
                    menuNum = int(input('2.NEW-ACCOUNT    99.SERVICE-OUT :  '))
                except ValueError:
                    print('Please enter a valid menu number!!')
                    continue
            
            if menuNum in (bank_config.ACCOUNT_LIST, bank_config.DEPOSIT, bank_config.WITHDRAWAL) and not self.accounts.get(session.getSignInedMemberId()):
                self.accounts = self.load_accounts()
                if not self.accounts.get(session.getSignInedMemberId()):
                    print('Please create an account first!!')
                    continue

            if menuNum == bank_config.ACCOUNT_LIST:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getSignInedMemberId()]

                for idx, myAccount in enumerate(myAccounts.keys()):
                    print('==================================================================================\n')
                    print(f"[{idx+1}]: {myAccount}: {myAccounts[myAccount]['balance']}")
                    print('----------------------------------------------------------------------------------\n')
                    print('날짜/시간 \t\t 내역 \t\t\t 입금 \t\t 출금')
                    for history in myAccounts[myAccount]['histories']:
                        if 'dAmount' in history:
                            print(f"{history['dRegData']} \t {history['dHistory']} \t\t\t {history['dAmount']}")
                        else:
                            print(f"{history['wRegData']} \t {history['wHistory']} \t\t\t\t\t {history['wAmount']}")
                    print()

            elif menuNum == bank_config.NEW_ACCOUNT:
                self.accounts = self.load_accounts()
                if session.getSignInedMemberId() not in self.accounts:
                    self.accounts[session.getSignInedMemberId()] = {}

                myAccounts = self.accounts[session.getSignInedMemberId()]
                myAccounts[str(uuid.uuid4())] = {
                    'balance': 0,
                    'histories': []
                }

                self.save_accounts(self.accounts)
                print('NEW-ACCOUNT SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_accounts(): {self.load_accounts()}')

            elif menuNum == bank_config.DEPOSIT:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getSignInedMemberId()]

                print('\n===My Accounts====================================================================')
                for idx, account in enumerate(myAccounts.keys()):
                    print(f'[{idx+1}]: {account}')
                print('==================================================================================\n')

                depositAccountNumber = ''
                while True:
                    depositAccountNumber = input('Enter deposit account number :  ')
                    if depositAccountNumber not in myAccounts:
                        print('The account was not found!!')
                        print('\n===My Accounts====================================')
                        for idx, account in enumerate(myAccounts.keys()):
                            print(f'[{idx+1}]: {account}')
                        print('==================================================\n')
                    else:
                        break

                try:
                    depositAmount = int(input('Enter deposit amount :  '))
                except ValueError:
                    print('Please enter a valid amount!!')
                    continue
                if depositAmount <= 0:
                    print('Amount must be greater than zero!!')
                    continue
                depositHistory = input('Enter deposit history :  ')
                deposit = {
                    'dAmount': depositAmount,
                    'dHistory': depositHistory,
                    'dRegData': util_time.getCurrentDateTime(),
                    'dModDate': util_time.getCurrentDateTime()
                }

                myAccounts[depositAccountNumber]['balance'] += depositAmount
                myAccounts[depositAccountNumber]['histories'].insert(0, deposit)

                self.save_accounts(self.accounts)
                print('DEPOSIT SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_account(): {self.load_accounts()}')

            elif menuNum == bank_config.WITHDRAWAL:
                self.accounts = self.load_accounts()
                myAccounts = self.accounts[session.getSignInedMemberId()]

                print('\n===My Accounts====================================')
                for idx, account in enumerate(myAccounts.keys()):
                    print(f'[{idx+1}]: {account}')
                print('==================================================\n')

                withdrawalAccountNumber = ''
                while True:
                    withdrawalAccountNumber = input('Enter withdrawal account number :  ')
                    if withdrawalAccountNumber not in myAccounts:
                        print('The account was not found!!')
                        print('\n===My Accounts====================================')
                        for idx, account in enumerate(myAccounts.keys()):
                            print(f'[{idx+1}]: {account}')
                        print('==================================================\n')
                    else:
                        break

                try:
                    withdrawalAmount = int(input('Enter withdrawal amount :  '))
                except ValueError:
                    print('Please enter a valid amount!!')
                    continue
                if withdrawalAmount <= 0:
                    print('Amount must be greater than zero!!')
                    continue
                withdrawalHistory = input('Enter withdrawal history :  ')
                withdrawal = {
                    'wAmount': withdrawalAmount,
                    'wHistory': withdrawalHistory,
                    'wRegData': util_time.getCurrentDateTime(),
                    'wModDate': util_time.getCurrentDateTime()
                }

                if withdrawalAmount > myAccounts[withdrawalAccountNumber]['balance']:
                    print('ERROR! CHECK BALANCE!!')
                else:
                    myAccounts[withdrawalAccountNumber]['balance'] -= withdrawalAmount
                    myAccounts[withdrawalAccountNumber]['histories'].insert(0, withdrawal)

                    self.save_accounts(self.accounts)
                    print('WITHDRAWAL SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_account(): {self.load_accounts()}')

            elif menuNum == bank_config.SERVICE_OUT:
                flag = False


if __name__ == '__main__':
    bankService = BankService()
    bankService.run()