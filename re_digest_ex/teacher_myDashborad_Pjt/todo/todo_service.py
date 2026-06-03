import config as root_config
from todo import config as todo_config
import session
import os
import json
from util import util_time

class TodoService:
    def __init__(self):
        self.todos = {}
        self.init_database()


    def init_database(self):
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
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)


    def load_todos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        

    def isMyTodos(self):
        allTodos = self.load_todos()
        if session.getSignInedMemberId() in allTodos:
            return True
        
        return False


##============================================================================================================#
			
    def replaceTodo(self):
        self.todos = self.load_todos()
        self.myTodos = self.todos[session.getSignInedMemberId()]
                    

    def checkedDev(self):                
        if root_config.DEV_MOD:
            print(f'self.load_todos: {self.load_todos()}')
            

    def re_saveTodo(self):
        self.save_todos(self.todos)


    def inputTodoWirte(self):
        self.replaceTodo()
        tText = input('Input new todo txt :  ')
        tExpDate = input('Input todo exprtation date(ex: 2026-06-02 09:05:05) :  ')
        
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
                        
            
    def todoWirtwe(self):
        self.inputTodoWirte()

##============================================================================================================#

    def todoReading(self):
        self.replaceTodo()
        for idx, myTodo in enumerate(myTodo):
            print('==================================================================================\n')
            print(f'[{idx+1}]')
            print(f"TEST: [{myTodo['tText']}]")
            print(f"EXPIRATIONDATE: [{myTodo['tExpDate']}]")
            print(f"REGISTER DATE: [{myTodo['tRegDate']}]")
            print(f"MODIFY DATE: [{myTodo['tModDate']}]")
            print(f"COMPLETE: [{myTodo['tComplete']}]")
                        
                        
    def todoRead(self):
        self.todoReading()

##============================================================================================================#

    def inputTodoUpdate(self):
        self.replaceTodo()
        for idx, myTodo in enumerate(self.myTodos):
            print('==================================================================================\n')
            print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
            print('----------------------------------------------------------------------------------\n')

        todoNumber = int(input('Enter the todo number :  '))
        tText = input('Input todo txt :  ')
        tExpDate = input('Input todo exprtation date(ex: 2026-06-02 09:05:05) :  ')

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
        self.inputTodoUpdate()

##============================================================================================================#

    def selectedTodoDelete(self):
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
        self.selectedTodoDelete()

##============================================================================================================#

    def checkingTodo(self):
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
        self.checkingTodo()
                
##============================================================================================================#
    def run(self):

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
                    self.todoWirtwe()
                    
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