import config as root_config
from memo import config as memo_config
import session
import os
import json

class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database()


    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/memos.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\lyh\python\python_ex\myDashboardPjt\db\memos.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_memos(self.memos)
        else:
            self.memos = self.load_memos()


        # 애플리케이션의 데이터를 JSON 파일에 저장하는 것
    def save_memos(self, memos):   # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)


        # JSON 파일을 읽어서 애플리케이션으로 데이터를 저장하는 것
    def load_memos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
    

    def isMyMemos(self):
        allMemos = self.load_memos()
        if session.getSignInedMemberId() in allMemos:
            return True
        
        return False
    
##============================================================================================================#
    
    def replaceMemo(self):
        self.memos = self.load_memos()
        self.myMemos = self.memos[session.getSignInedMemberId()]

        
    def checkedDev(self):
        if root_config.DEV_MOD:
            print(f'self.load_memos: {self.load_memos()}')


    def re_saveMemo(self):
        self.save_memos(self.memos)


    def inputMemoWrite(self):        
        newMemo = input('Write new memo :  ')

        self.replaceMemo()
        self.myMemos.insert(0, newMemo)

        self.re_saveMemo()
        print('WRITE SUCCESS!!')
        
        self.checkedDev()
            
            
    def memoWrite(self):
        self.inputMemoWrite()
					
##============================================================================================================#	  

    def memoReading(self):
        self.replaceMemo()
        for idx, memo in enumerate(self.myMemos):
            print('==================================================================================\n')
            print(f'[{idx+1}] {memo}')
                        

    def memoRead(self):
        self.memoReading()

##============================================================================================================#	  

    def inputMemoUpdate(self):
        self.replaceMemo()
        for idx, memo in enumerate(self.myMemos):
            print('==================================================================================\n')
            print(f'[{idx+1}] {memo}')

        selectedNumber = int(input('Please select the number to modify :  '))
        memo = input('Edit memo :  ')
        self.myMemos[selectedNumber-1] = memo

        self.re_saveMemo()
        print('MODIFY SUCCESS!!')

        self.checkedDev()
                        
                        
    def memoUpdate(self):
        self.inputMemoUpdate()

##============================================================================================================#	  

    def selectedMemoDelete(self):
        self.replaceMemo()
        for idx, memo in enumerate(self.myMemos):
            print(f'[{idx+1}] {memo}')

        selectedNumber = int(input('Please select the number to delete :  '))
        self.myMemos.pop(selectedNumber-1)
        self.re_saveMemo()

        self.checkedDev()
            

    def memoDelete(self):
        self.selectedMemoDelete()
        
##============================================================================================================#	  				
    def run(self):

            if session.getSignInedMemberId() == '':
                print('Please SIGN-IN!!')
                return
            
            flag = True
            while flag:

                if not self.isMyMemos():
                    self.memos[session.getSignInedMemberId()] = []
                    self.re_saveMemo()
                
                menuNum = int(input('1.WRITE    2.READ    3.UPDATE    4.DELETE    99.SERVICE-OUT :  '))
                
                if menuNum == memo_config.WRITE:
                    self.memoWrite()
                    
                elif menuNum == memo_config.READ:
                    self.memoRead()
                    
                elif menuNum == memo_config.UPDATE:
                    self.memoUpdate()
                    
                elif menuNum == memo_config.DELETE:
                    self.memoDelete()
                    
                elif menuNum == memo_config.SERVICE_OUT:
                    flag = False


if __name__ == '__main__':
    memoService = MemoService()
    memoService.run()