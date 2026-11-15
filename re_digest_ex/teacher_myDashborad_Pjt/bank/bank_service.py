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
		'''계좌 딕셔너리를 JSON 파일에 저장한다.'''
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

##============================================================================================================#	    

	def replaceAccounts(self):
		'''파일에서 계좌를 다시 읽어 로그인한 회원의 계좌만 myAccounts 에 담는다.'''
		self.accounts = self.load_accounts()
		self.myAccounts = self.accounts[session.getSignInedMemberId()]
		print()
						

	def printedAcctList(self):
		'''회원의 계좌별 잔액과 입금·출금 내역을 출력한다.'''
		for idx, myAccount in enumerate(self.myAccounts.keys()):
			print('==================================================================================\n')
			print(f"[{idx+1}]: {myAccount}: {self.myAccounts[myAccount]['balance']}")
			print('----------------------------------------------------------------------------------\n')
			print('날짜/시간 \t\t 내역 \t\t\t 입금 \t\t 출금')
			for history in self.myAccounts[myAccount]['histories']:
				if 'dAmount' in history:
					print(f"{history['dRegData']} \t {history['dHistory']} \t\t\t {history['dAmount']}")
				else:
					print(f"{history['wRegData']} \t {history['wHistory']} \t\t\t\t\t {history['wAmount']}")
			print()
		
		
	def accountList(self):
		'''최신 계좌 정보를 불러와 계좌 목록을 출력한다.'''
		self.replaceAccounts()
		self.printedAcctList()

##============================================================================================================#		

	def findedAccounts(self):
		'''계좌를 불러오고, 로그인한 회원 항목이 없으면 빈 딕셔너리로 만든다.'''
		self.accounts = self.load_accounts()
		if session.getSignInedMemberId() not in self.accounts:
			self.accounts[session.getSignInedMemberId()] = {}


	def createdUuidAcct(self):
		'''잔액 0 의 새 계좌를 UUID 번호로 만든다.'''
		self.myAccounts = self.accounts[session.getSignInedMemberId()]
		self.myAccounts[str(uuid.uuid4())] = {
			'balance': 0,
			'histories': []
			}


	def checkedDev(self):
		'''개발 모드일 때만 저장된 계좌 전체를 출력한다.'''
		if root_config.DEV_MOD:
			print(f'self.load_accounts(): {self.load_accounts()}')


	def reportedAccounts(self):
		'''계좌를 파일에 저장하고 개설 성공을 알린다.'''
		self.save_accounts(self.accounts)
		print('NEW-ACCOUNT SUCCESS!!')

		self.checkedDev()


	def newAccount(self):
		'''새 계좌를 개설해 저장하는 전체 흐름을 처리한다.'''
		self.findedAccounts()
		self.createdUuidAcct()
		self.reportedAccounts()

##============================================================================================================#	

	def choosedDeposit(self):
		'''입금할 계좌 번호를 올바르게 입력할 때까지 받고 입금 입력으로 넘긴다.'''
		print('\n===My Accounts====================================================================')
		for idx, account in enumerate(self.myAccounts.keys()):
			print(f'[{idx+1}]: {account}')
		print('==================================================================================\n')

		self.depositAccountNumber = ''
		while True:
			self.depositAccountNumber = input('Enter deposit account number :  ')
			if self.depositAccountNumber not in self.myAccounts:
				print('The account was not found!!')
				print('\n===My Accounts====================================')
				for idx, account in enumerate(self.myAccounts.keys()):
					print(f'[{idx+1}]: {account}')
				print('==================================================\n')
			else:
				break

		self.inputDeposit()


	def inputDeposit(self):
		'''입금액과 내역을 입력받아 입금 기록을 만든다.'''
		self.depositAmount = int(input('Enter deposit amount :  '))
		self.depositHistory = input('Enter deposit history :  ')
		self.deposit = {
			'dAmount': self.depositAmount,
			'dHistory': self.depositHistory,
			'dRegData': util_time.getCurrentDateTime(),
			'dModDate': util_time.getCurrentDateTime()
			}

		self.depositBalance()


	def depositBalance(self):
		'''선택한 계좌의 잔액을 늘리고 입금 내역을 맨 앞에 추가해 저장한다.'''
		self.myAccounts[self.depositAccountNumber]['balance'] += self.depositAmount
		self.myAccounts[self.depositAccountNumber]['histories'].insert(0, self.deposit)

		self.save_accounts(self.accounts)
		print('DEPOSIT SUCCESS!!')

		self.checkedDev()


	def deposit(self):
		'''최신 계좌를 불러와 입금 절차를 시작한다.'''
		self.replaceAccounts()
		self.choosedDeposit()

##============================================================================================================#	

	def choosedWithdrawal(self):
		'''출금할 계좌 번호를 올바르게 입력할 때까지 받고 출금 입력으로 넘긴다.'''
		print('\n===My Accounts====================================')
		for idx, account in enumerate(self.myAccounts.keys()):
			print(f'[{idx+1}]: {account}')
		print('==================================================\n')

		self.withdrawalAccountNumber = ''
		while True:
			self.withdrawalAccountNumber = input('Enter withdrawal account number :  ')
			if self.withdrawalAccountNumber not in self.myAccounts:
				print('The account was not found!!')
				print('\n===My Accounts====================================')
				for idx, account in enumerate(self.myAccounts.keys()):
					print(f'[{idx+1}]: {account}')
				print('==================================================\n')
			else:
				break

		self.inputWithdrawal()


	def inputWithdrawal(self):
		'''출금액과 내역을 입력받아 출금 기록을 만든다.'''
		self.withdrawalAmount = int(input('Enter withdrawal amount :  '))
		self.withdrawalHistory = input('Enter withdrawal history :  ')
		self.withdrawal = {
			'wAmount': self.withdrawalAmount,
			'wHistory': self.withdrawalHistory,
			'wRegData': util_time.getCurrentDateTime(),
			'wModDate': util_time.getCurrentDateTime()
			}

		self.zeroInput()


	def zeroInput(self):
		'''잔액이 부족하면 오류를 알리고, 충분하면 잔액을 줄이고 출금 내역을 저장한다.'''
		if self.withdrawalAmount > self.myAccounts[self.withdrawalAccountNumber]['balance']:
			print('ERROR! CHECK BALANCE!!')
			return

		self.myAccounts[self.withdrawalAccountNumber]['balance'] -= self.withdrawalAmount
		self.myAccounts[self.withdrawalAccountNumber]['histories'].insert(0, self.withdrawal)

		self.save_accounts(self.accounts)
		print('WITHDRAWAL SUCCESS!!')

		self.checkedDev()


	def withdrawal(self):
		'''최신 계좌를 불러와 출금 절차를 시작한다.'''
		self.replaceAccounts()
		self.choosedWithdrawal()


	def run(self):
		'''로그인 확인 후 계좌 목록·개설·입금·출금 메뉴를 반복 처리한다.'''

		if session.getSignInedMemberId() == '':
			print('Please SIGN-IN!!')
			return

		flag = True
		while flag:

			if self.isMyAccount():
				menuNum = int(input('1.ACCOUNT-LIST    2.NEW-ACCOUNT    3.DEPOSIT    4.WITHDRAWAL    99.SERVICE-OUT :  '))
			
			else:
				print('No account yet!!')
				menuNum = int(input('2.NEW-ACCOUNT    99.SERVICE-OUT :  '))

			if menuNum == bank_config.ACCOUNT_LIST:
				self.accountList()

			elif menuNum == bank_config.NEW_ACCOUNT:
				self.newAccount()

			elif menuNum == bank_config.DEPOSIT:
				self.deposit()

			elif menuNum == bank_config.WITHDRAWAL:
				self.withdrawal()

			elif menuNum == bank_config.SERVICE_OUT:
				flag = False


if __name__ == '__main__':
	bankService = BankService()
	bankService.run()