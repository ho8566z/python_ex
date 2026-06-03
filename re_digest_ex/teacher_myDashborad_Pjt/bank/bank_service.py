import config as root_config
from bank import config as bank_config
import session
import os
import json
import uuid
from util import util_time

class BankService:
	def __init__(self):
		self.accounts = {}
		self.init_database()


	def init_database(self):
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
		with open(self.dbFile, 'w', encoding='utf-8') as f:
			json.dump(accounts, f, ensure_ascii=False, indent=4)


	def load_accounts(self):
		with open(self.dbFile, 'r', encoding='utf-8') as f:
			return json.load(f)


	def isMyAccount(self):
		allAcccounts = self.load_accounts()
		if session.getSignInedMemberId() in allAcccounts:
			return True

		return False

##============================================================================================================#	    

	def replaceAccounts(self):
		self.accounts = self.load_accounts()
		self.myAccounts = self.accounts[session.getSignInedMemberId()]
		print()
						

	def printedAcctList(self):
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
		self.replaceAccounts()
		self.printedAcctList()

##============================================================================================================#		

	def findedAccounts(self):
		self.accounts = self.load_accounts()
		if session.getSignInedMemberId() not in self.accounts:
			self.accounts[session.getSignInedMemberId()] = {}


	def createdUuidAcct(self):
		self.myAccounts = self.accounts[session.getSignInedMemberId()]
		self.myAccounts[str(uuid.uuid4())] = {
'balance': 0,
'histories': []
}


	def checkedDev(self):
		if root_config.DEV_MOD:
			print(f'self.load_accounts(): {self.load_accounts()}')


	def reportedAccounts(self):
		self.save_accounts(self.accounts)
		print('NEW-ACCOUNT SUCCESS!!')

		self.checkedDev()


	def newAccount(self):
		self.findedAccounts()
		self.createdUuidAcct()
		self.reportedAccounts()

##============================================================================================================#	

	def choosedDeposit(self):
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
		self.myAccounts[self.depositAccountNumber]['balance'] += self.depositAmount
		self.myAccounts[self.depositAccountNumber]['histories'].insert(0, self.deposit)

		self.save_accounts(self.accounts)
		print('DEPOSIT SUCCESS!!')

		self.checkedDev()


	def deposit(self):
		self.replaceAccounts()
		self.choosedDeposit()

##============================================================================================================#	

	def choosedWithdrawal(self):
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
		if self.withdrawalAmount > self.myAccounts[self.withdrawalAccountNumber]['balance']:
			print('ERROR! CHECK BALANCE!!')
		else:
			self.myAccounts[self.withdrawalAccountNumber]['balance'] -= self.withdrawalAmount
			self.myAccounts[self.withdrawalAccountNumber]['histories'].insert(0, self.withdrawal)

		self.save_accounts(self.accounts)
		print('WITHDRAWAL SUCCESS!!')

		self.checkedDev()


	def withdrawal(self):
		self.replaceAccounts()
		self.choosedWithdrawal()


	def run(self):

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