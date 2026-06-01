import config
from member import member_service
from bank import bank_service

def main():
    flag = True
    while flag:
        menuNum = int(input('1.MEMBER    2.BANK    3.MEMO    4.TODO    99.SYSTEM-OUT '))
        if menuNum == config.MEMBER_SERVICE:
            memberSerive = member_service.MemberSerive()
            memberSerive.run()

        elif menuNum == config.BANK_SERVICE:
            bankService = bank_service.BankService()
            bankService.run()

        elif menuNum == config.MEMO_SERVICE:
            pass

        elif menuNum == config.TODO_SERVICE:
            pass

        elif menuNum == config.SYSTEM_OUT:
            flag = False
        

if __name__ == "__main__":
    main()