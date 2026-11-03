import config
from member import member_service
from bank import bank_service
from memo import memo_service
from todo import todo_service

# 메뉴 번호에 맞는 서비스를 골라 실행하는 진입 함수
def main():
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER    2.BANK    3.MEMO    4.TODO    99.SYSTEM-OUT :  '))
        if menuNum == config.MEMBER_SERVICE:
            member_service.MemberService().run()

        elif menuNum == config.BANK_SERVICE:
            bank_service.BankService().run()
            
        elif menuNum == config.MEMO_SERVICE:
            memo_service.MemoService().run()
            
        elif menuNum == config.TODO_SERVICE:
            todo_service.TodoService().run()
            
        # 종료 번호를 고르면 반복문을 멈춘다
        elif menuNum == config.SYSTEM_OUT:
            flag = False
        

if __name__ == "__main__":
    main()