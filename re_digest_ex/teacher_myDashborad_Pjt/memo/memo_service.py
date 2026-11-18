import config as root_config
from memo import config as memo_config
import session
import os
import json

class MemoService:
    '''로그인한 회원의 메모를 관리하고 memos.json 에 저장하는 서비스 클래스.'''
    def __init__(self):
        '''메모 저장소를 비우고 데이터베이스를 초기화한다.'''
        self.memos = {}
        self.init_database()


    def init_database(self):
        '''db/memos.json 경로를 정하고, 파일이 없으면 새로 만들고 있으면 불러온다.'''
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


    def save_memos(self, memos):   # {}
        """애플리케이션의 데이터를 JSON 파일에 저장한다."""
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)


    def load_memos(self):
        """JSON 파일을 읽어서 애플리케이션으로 데이터를 불러온다."""
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
    

    def isMyMemos(self):
        '''로그인한 회원의 메모 목록이 이미 있는지 반환한다.'''
        allMemos = self.load_memos()
        if session.getSignInedMemberId() in allMemos:
            return True
        
        return False
    
##============================================================================================================#
    
    def replaceMemo(self):
        '''파일에서 메모를 다시 읽어 로그인한 회원의 메모만 myMemos 에 담는다.'''
        self.memos = self.load_memos()
        self.myMemos = self.memos[session.getSignInedMemberId()]

        
    def checkedDev(self):
        '''개발 모드일 때만 저장된 메모 전체를 출력한다.'''
        if root_config.DEV_MOD:
            print(f'self.load_memos: {self.load_memos()}')


    def re_saveMemo(self):
        '''현재 메모 딕셔너리를 JSON 파일에 다시 저장한다.'''
        self.save_memos(self.memos)


    def inputMemoWrite(self):        
        '''새 메모를 입력받아 목록 맨 앞에 추가하고 저장한다.'''
        newMemo = input('Write new memo :  ')

        self.replaceMemo()
        self.myMemos.insert(0, newMemo)

        self.re_saveMemo()
        print('WRITE SUCCESS!!')
        
        self.checkedDev()
            
            
    def memoWrite(self):
        '''메모 작성 입력 흐름을 실행한다.'''
        self.inputMemoWrite()
					
##============================================================================================================#	  

    def memoReading(self):
        '''로그인한 회원의 메모 목록을 번호와 함께 모두 출력한다.'''
        self.replaceMemo()
        for idx, memo in enumerate(self.myMemos):
            print('==================================================================================\n')
            print(f'[{idx+1}] {memo}')
                        

    def memoRead(self):
        '''메모 조회 흐름을 실행한다.'''
        self.memoReading()

##============================================================================================================#	  

    def inputMemoUpdate(self):
        '''수정할 메모 번호와 새 내용을 입력받아 해당 메모를 바꾸고 저장한다.'''
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
        '''메모 수정 입력 흐름을 실행한다.'''
        self.inputMemoUpdate()

##============================================================================================================#	  

    def selectedMemoDelete(self):
        '''삭제할 메모 번호를 입력받아 해당 메모를 지우고 저장한다.'''
        self.replaceMemo()
        for idx, memo in enumerate(self.myMemos):
            print(f'[{idx+1}] {memo}')

        selectedNumber = int(input('Please select the number to delete :  '))
        self.myMemos.pop(selectedNumber-1)
        self.re_saveMemo()

        self.checkedDev()
            

    def memoDelete(self):
        '''메모 삭제 입력 흐름을 실행한다.'''
        self.selectedMemoDelete()
        
##============================================================================================================#	  				
    def run(self):
            '''로그인 확인 후 메모 작성·조회·수정·삭제 메뉴를 반복 처리한다.'''

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