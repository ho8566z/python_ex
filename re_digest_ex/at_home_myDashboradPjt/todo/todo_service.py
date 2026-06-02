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


    def run(self):

        if session.getSignInedMemberId() == '':
            print('Please SIGN-IN!!')
            return
        
        flag = True
        while flag:
            if not self.isMyTodos():
                self.todos[session.getSignInedMemberId()] = []
                self.save_todos(self.todos)

            memuNum = int(input('1.WRITE    2.READ    3.UPDATE    4.DELETE    5.COMPLETE-CHANGE    99.SERVICE-OUT :  '))
            if memuNum == todo_config.WRITE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                
                tText = input('Input new todo txt :  ')
                tExpDate = input('Input todo exprtation date(ex: 2026-06-02 09:05:05) :  ')
                
                todo = {
                    'tText': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': util_time.getCurrentDateTime(),
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': False
                }

                myTodos.insert(0, todo)
                self.save_todos(self.todos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos: {self.load_todos()}')

            elif memuNum == todo_config.READ:
                self.todos = self.load_todos()      # dic
                myTodo = self.todos[session.getSignInedMemberId()] # list
                for idx, myTodo in enumerate(myTodo):
                    print('==================================================================================\n')
                    print(f'[{idx+1}]')
                    print(f"TEST: [{myTodo['tText']}]")
                    print(f"EXPIRATIONDATE: [{myTodo['tExpDate']}]")
                    print(f"REGISTER DATE: [{myTodo['tRegDate']}]")
                    print(f"MODIFY DATE: [{myTodo['tModDate']}]")
                    print(f"COMPLETE: [{myTodo['tComplete']}]")

            elif memuNum == todo_config.UPDATE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('==================================================================================\n')
                    print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
                    print('----------------------------------------------------------------------------------\n')

                todoNumber = int(input('Enter the todo number :  '))
                tText = input('Input todo txt :  ')
                tExpDate = input('Input todo exprtation date(ex: 2026-06-02 09:05:05) :  ')

                todo = {
                    'tText': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': myTodos[todoNumber-1]['tRegDate'],
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': myTodos[todoNumber-1]['tComplete']
                }

                myTodos[todoNumber-1] = todo
                self.save_todos(self.todos)
                print('UPDATE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos: {self.load_todos()}')

            elif memuNum == todo_config.DELETE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('==================================================================================\n')
                    print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
                    print('----------------------------------------------------------------------------------\n')

                todoNumber = int(input('Enter the todo number :  '))
                myTodos.pop(todoNumber-1)
                # DEL버전: del myTodos[todoNumber-1]
                self.save_todos(self.todos)

                if root_config.DEV_MOD:
                    print(f'self.load_todos: {self.load_todos()}')

            elif memuNum == todo_config.COMPLETE_CHANGE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx, myTodo in enumerate(myTodos):
                    print('==================================================================================\n')
                    print(f"[{idx+1}] {myTodo['tText']} [{myTodo['tExpDate']}][{myTodo['tComplete']}]")
                    print('----------------------------------------------------------------------------------\n')

                todoNumber = int(input('Enter the todo number :  '))
                myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
                self.save_todos(self.todos)
                print('COMPLETE CHANGE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos: {self.load_todos()}')
                
            elif memuNum == todo_config.SERVICE_OUT:
                flag = False


if __name__ == '__main__':
    todoService = TodoService()
    todoService.run()