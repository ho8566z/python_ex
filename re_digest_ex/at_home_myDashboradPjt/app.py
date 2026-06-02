import config
from member import member_service
from bank import bank_service
from memo import memo_service
from todo import todo_service

def main():
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER    2.BANK    3.MEMO    4.TODO    99.SYSTEM-OUT :  '))
        if menuNum == config.MEMBER_SERVICE:
            member_service.MemberSerive().run()
            # memberSerive = member_service.MemberSerive()
            # memberSerive.run()

        elif menuNum == config.BANK_SERVICE:
            bank_service.BankService().run()
            # bankService = bank_service.BankService()
            # bankService.run()

        elif menuNum == config.MEMO_SERVICE:
            memo_service.MemoService().run()
            # MemoService = memo_service.MemoService()
            # MemoService.run()

        elif menuNum == config.TODO_SERVICE:
            todo_service.TodoService().run()
            # TodoService = todo_service.TodoService()
            # TodoService.run()

        elif menuNum == config.SYSTEM_OUT:
            flag = False
        

if __name__ == "__main__":
    main()