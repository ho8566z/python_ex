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
    

    def run(self):

        if session.getSignInedMemberId() == '':
            print('Please SIGN-IN!!')
            return
        
        flag = True
        while flag:

            if not self.isMyMemos():
                self.memos[session.getSignInedMemberId()] = []
                self.save_memos(self.memos)
            
            menuNum = int(input('1.WRITE    2.READ    3.UPDATE    4.DELETE    99.SERVICE-OUT :  '))
            
            if menuNum == memo_config.WRITE:
                newMemo = input('Write new memo :  ')

                self.memos = self.load_memos()
                myMemos = self.memos[session.getSignInedMemberId()]
                myMemos.insert(0, newMemo)

                self.save_memos(self.memos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos: {self.load_memos()}')

            elif menuNum == memo_config.READ:
                self.memos = self.load_memos()      # dic
                myMemos = self.memos[session.getSignInedMemberId()] # list
                for idx, memo in enumerate(myMemos):
                    print('==================================================================================\n')
                    print(f'[{idx+1}] {memo}')

            elif menuNum == memo_config.UPDATE:
                self.memos = self.load_memos()      # dic
                myMemos = self.memos[session.getSignInedMemberId()] # list
                for idx, memo in enumerate(myMemos):
                    print('==================================================================================\n')
                    print(f'[{idx+1}] {memo}')

                selectedNumber = int(input('Please select the number to modify :  '))
                memo = input('Edit memo :  ')
                myMemos[selectedNumber-1] = memo

                self.save_memos(self.memos)
                print('MODIFY SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_memos: {self.load_memos()}')

            elif menuNum == memo_config.DELETE:
                self.memos = self.load_memos()      # dic
                myMemos = self.memos[session.getSignInedMemberId()] # list
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')

                selectedNumber = int(input('Please select the number to delete :  '))
                myMemos.pop(selectedNumber-1)
                self.save_memos(self.memos)

                if root_config.DEV_MOD:
                    print(f'self.load_memos: {self.load_memos()}')
                
            elif menuNum == memo_config.SERVICE_OUT:
                flag = False


if __name__ == '__main__':
    memoService = MemoService()
    memoService.run()