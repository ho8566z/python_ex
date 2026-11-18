import config as root_config
from todo import config as todo_config
import session
import os
import json
from util import util_time

class TodoService:
    '''로그인한 회원의 할 일을 작성·조회·수정·삭제하고 todos.json 에 저장하는 서비스 클래스.'''
    def __init__(self):
        """빈 할 일 저장소를 만들고 db/todos.json 파일을 준비한다."""
        self.todos = {}
        self.init_database()


    def init_database(self):
        """db/todos.json 경로를 정하고, 파일이 없으면 새로 저장하고 있으면 읽어 온다."""
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/todos.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')
        print(f'self.dbFile: {self.dbFile}')
        #C:\lyh\python\python_ex\myDashboardPjt\db\todos.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_todos(self.todos)
        else:
            self.todos = self.load_todos()


    # JSON 파일 저장
    def save_todos(self, todos):   # {}
        """전체 할 일 딕셔너리를 JSON 파일에 저장한다."""
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)


    def load_todos(self):
        """JSON 파일에서 전체 할 일 딕셔너리를 읽어 반환한다."""
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        

    def isMyTodos(self):
        """로그인한 회원의 할 일 목록이 파일에 이미 있는지 반환한다."""
        allTodos = self.load_todos()
        if session.getSignInedMemberId() in allTodos:
            return True
        
        return False


##============================================================================================================#
			
    def replaceTodo(self):
        """파일의 최신 할 일을 읽어 로그인한 회원의 목록myTodos으로 갈아 끼운다."""
        self.todos = self.load_todos()
        self.myTodos = self.todos[session.getSignInedMemberId()]
                    

    def checkedDev(self):                
        '''개발 모드일 때만 현재 파일에 저장된 할 일 전체를 출력한다.'''
        if root_config.DEV_MOD:
            print(f'self.load_todos: {self.load_todos()}')
            

    def re_saveTodo(self):
        """메모리의 할 일 전체를 파일에 다시 저장한다."""
        self.save_todos(self.todos)


    def inputTodoWrite(self):
        """내용과 만료일을 입력받아 새 할 일을 목록 맨 앞에 추가하고 저장한다."""
        self.replaceTodo()
        tText = input('Input new todo txt :  ')
        tExpDate = input('Input todo expiration date(ex: 2026-06-02 09:05:05) :  ')
        
        self.todo = {
            'tText': tText,
            'tExpDate': tExpDate,
            'tRegDate': util_time.getCurrentDateTime(),
            'tModDate': util_time.getCurrentDateTime(),
            'tComplete': False
        }
        
        self.myTodos.insert(0, self.todo)
        self.re_saveTodo()
        print('WRITE SUCCESS!!')

        self.checkedDev()
                        
            
    def todoWrite(self):
        '''할 일 작성 입력 흐름을 실행한다.'''
        self.inputTodoWrite()

##============================================================================================================#

    def todoReading(self):
        '''로그인한 회원의 할 일 목록을 번호와 함께 모두 출력한다.'''
        self.replaceTodo()
        for idx, myTodo in enumerate(self.myTodos):
            print('==================================================================================\n')
            print(f'[{idx+1}]')
            print(f"TEXT: [{myTodo['tText']}]")
            print(f"EXPIRATIONDATE: [{myTodo['tExpDate']}]")
            print(f"REGISTER DATE: [{myTodo['tRegDate']}]")
            print(f"MODIFY DATE: [{myTodo['tModDate']}]")
            print(f"COMPLETE: [{myTodo['tComplete']}]")
                        
                        
    def todoRead(self):
        '''할 일 목록을 조회한다.'''
        self.todoReading()

##============================================================================================================#

    def inputTodoUpdate(self):
        """번호를 골라 내용과 만료일을 고치고 수정일을 갱신해 저장한다. 등록일과 완료 여부는 유지한다."""
        self.replaceTodo()
        for idx, myTodo in enumerate(self.myTodos):
            print('==================================================================================\n')
            print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
            print('----------------------------------------------------------------------------------\n')

        todoNumber = int(input('Enter the todo number :  '))
        tText = input('Input todo txt :  ')
        tExpDate = input('Input todo expiration date(ex: 2026-06-02 09:05:05) :  ')

        self.todo = {
            'tText': tText,
            'tExpDate': tExpDate,
            'tRegDate': self.myTodos[todoNumber-1]['tRegDate'],
            'tModDate': util_time.getCurrentDateTime(),
            'tComplete': self.myTodos[todoNumber-1]['tComplete']
        }

        self.myTodos[todoNumber-1] = self.todo
        self.re_saveTodo()
        print('UPDATE SUCCESS!!')

        self.checkedDev()
                        
                        
    def todoUpdate(self):
        '''할 일 내용을 수정한다.'''
        self.inputTodoUpdate()

##============================================================================================================#

    def selectedTodoDelete(self):
        '''목록을 번호와 함께 보여 주고, 입력받은 번호의 할 일을 지운 뒤 저장한다.'''
        self.replaceTodo()
        for idx, myTodo in enumerate(self.myTodos):
            print('==================================================================================\n')
            print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
            print('----------------------------------------------------------------------------------\n')

        todoNumber = int(input('Enter the todo number :  '))
        self.myTodos.pop(todoNumber-1)
        self.re_saveTodo()

        self.checkedDev()
                        
                        
    def todoDelete(self):
        '''할 일 삭제 메뉴를 실행한다.'''
        self.selectedTodoDelete()

##============================================================================================================#

    def checkingTodo(self):
        """번호를 골라 해당 할 일의 완료 여부를 반대로 바꾸고 저장한다."""
        self.replaceTodo()
        for idx, myTodo in enumerate(self.myTodos):
            print('==================================================================================\n')
            print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
            print('----------------------------------------------------------------------------------\n')

        todoNumber = int(input('Enter the todo number :  '))
        self.myTodos[todoNumber-1]['tComplete'] = not self.myTodos[todoNumber-1]['tComplete']
        self.re_saveTodo()
        print('COMPLETE CHANGE SUCCESS!!')

        self.checkedDev()
                        
        
    def completeChange(self):
        '''할 일의 완료 상태를 바꾼다.'''
        self.checkingTodo()
                
##============================================================================================================#
    def run(self):
            '''로그인 상태에서 할 일 메뉴(작성·조회·수정·삭제·완료 변경)를 반복 실행한다.'''

            if session.getSignInedMemberId() == '':
                print('Please SIGN-IN!!')
                return
            
            flag = True
            while flag:
                if not self.isMyTodos():
                    self.todos[session.getSignInedMemberId()] = []
                    self.re_saveTodo()

                memuNum = int(input('1.WRITE    2.READ    3.UPDATE    4.DELETE    5.COMPLETE-CHANGE    99.SERVICE-OUT :  '))
                if memuNum == todo_config.WRITE:
                    self.todoWrite()
                    
                elif memuNum == todo_config.READ:
                    self.todoRead()
                    
                elif memuNum == todo_config.UPDATE:
                    self.todoUpdate()
                    
                elif memuNum == todo_config.DELETE:
                    self.todoDelete()
                    
                elif memuNum == todo_config.COMPLETE_CHANGE:
                    self.completeChange()
                    
                elif memuNum == todo_config.SERVICE_OUT:
                    flag = False


if __name__ == '__main__':
    todoService = TodoService()
    todoService.run()