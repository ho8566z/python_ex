import os       #현재 실행 중인 파이썬 파일의 절대 경로를 가져온다
import sys      #위에서 얻은 파일 경로에서 파일 이름을 제외한 폴더 경로를 추출한다
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#현재 파일이 위치한 폴더의 상위 폴더 경로를 파이썬 모듈 검색 경로에 추가하여, 상위 폴더 내의 모듈을 불러올 수 있게 만듦

import session                  #로그인 상태를 검증하는 모듈 파일을 소환(import)한다
import datetime                 #날짜 및 시간을 확인 가능한 모듈을 소환
import copy                     #데이터를 복사할 수 있는 모듈을 소환
import json                     #json형식으로 파일을 관리가능한 모듈을 소환
from db import config           #'db'디렉토리에서 'config(상수)'모듈을 소환
from db import backAccountDb    #'db'디렉토리에서 'backAccountDb(계좌 더미 데이터)'모듈을 소환

ADD_MONEY = 1           #상수: 입금 = '1'로 할당
SUB_MONEY = 2           #상수: 출금 = '2'로 할당
MONEY_FLOW = 3          #상수: 입출 내역 = '3'로 할당
SELECT_END = 99         #상수: 입출메뉴 종료 = '99'로 할당

flag = True             #flag(깃발)변수 = True(참)으로 할당
accountBalance = 0      #'계좌 잔액' 데이터에 입출 내역에 따라 데이터를 기록하기 전에 '0'으로 할당


def startLoop():                #함수: start한다, loop(루프)를
    if session.onSignIned:      #1번째 만약에, 로그인 상태를 확인했을 때, 로그인 중이라면
        if config.BANK_ACNT:    #2번째 만약에, (모듈)은행 계좌번호가 있다면
            setMoneyFlow()      #'set한다, money의 flow를' 함수를 실행한다

        else:                   #2번째 만약이 아니라면,
            setBankAccount()    #'set한다, bank의 account를' 함수를 실행한다
            return              #함수가 끝나면, 되돌아가라
        
    else:                       #1번째 만약이 아니라면, ->//
        print('로그인을 진행한 다음, 진행하세요.')  #'로그인이 우선이라는 메세지'를 출력해라
        return                  #//-> 되돌아가라


def setBankAccount():           #함수: set한다, bank의 account를
    fixedNumber = '101-77'      #고정 번호는 '101-77'이다
    userAccount = 'id'          #사용자 번호는 '회원id'이다
    bankAccount = f'{fixedNumber}-{userAccount}'    
    #은행 계좌번호는 f'{고정 번호}-{사용자 번호}'으로 할당된다
    #-> 계좌번호ex) '101-77-jungho(회원id)'
    config.BANK_ACNT = bankAccount      #(모듈)은행 계좌번호는 '계좌번호(101-77-회원id)'를 할당한다
    try:        #시도해라
        inputAccountPw = int(input('계좌 비밀번호 입력: '))     #'입력받은 계좌 비밀번호'는 input되어 int로 캐스팅된 데이터이다
        print('계좌 비밀번호가 설정되었습니다.')        #'계좌 비밀번호 설정이 완료되었다'는 메세지를 출력해라
        config.BANK_PW = inputAccountPw             #(모듈)은행 비밀번호는 '입력받은 계좌 비밀번호'를 할당한다

    except ValueError:      #try해서 value에서 error가 생긴다면,
        print('비밀번호를 다시 입력하세요.')            #'비밀번호를 재입력 해라'라는 메세지를 출력해라

    backAccountDb.bankAccountDb[config.BANK_ACNT] = {   
        #(파일)은행계좌 데이터베이스.(딕셔너리)은행계좌 데이터베이스.[(모듈)은행 계좌번호] = {딕셔너리}
        config.BANK_ACNT: {     #'(모듈)은행 계좌번호'는 : {딕셔너리}
        config.BANK_ACNT: bankAccount,      #(모듈)은행 계좌번호는 '계좌번호(101-77-회원id)'가 해당한다
        config.BANK_PW: inputAccountPw,     #(모듈)은행 비밀번호는 '입력받은 계좌 비밀번호'가 해당한다
        config.BANK_LOG: []                 #(모듈)은행 기록은 []리스트가 해당한다
        }
    }

    print(f'Bank_Account created: {config.BANK_ACNT}')  #'은행계좌 생성완료'라는 메세지를 출력해라
    return config.BANK_ACNT                             #'(모듈)은행 계좌번호' 데이터를 반환해라


def addMoney():                 #함수: add한다, money를
    global accountBalance       #전역변수 accountBalance를 지역변수로서 사용 가능하도록

    try:        #시도해라
        plus = int(input('금액을 입력하세요, 입금 금액: '))     #'더하기'는 input되어 int로 캐스팅된 '입금할 금액'이다
        if plus <= 0:           #만약에, '더하기'가 0보다 작거나 같다면 ->//
            print('0원 이하 금액은 입금할 수 없습니다.')        #//-> '입금이 불가하다'는 메세지를 출력해라
            return              #되돌아가라
        else:                   #만약이 아니라면,
            print('입금 중입니다.')     #'입금 중'이라는 메세지를 출력해라
            accountBalance += plus     #'계좌 잔액'에 '더하기'의 값(입금할 금액)를 더해라
            now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            #'지금'은 '(모듈)날짜.지금날짜.지금()'을 문자열로 바꿔라, 
            # '%Y-%m-%d %H-%M-%S(2026-05-28 22-22-16)'의 형식으로
            backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG].append(
                #(파일)은행계좌 데이터베이스.(딕셔너리)은행계좌 데이터베이스.[(모듈)은행 계좌번호]
                # [(모듈)은행 계좌번호][(모듈)은행 계좌기록]에 추가해라,
                (now, plus, '입금')
                #'지금시각, 더하기(입금 금액), "입금"'의 양식대로 입금 데이터를
            )
            print(f'입금 완료, 현재 잔액: {accountBalance:,}원')
            #'입금 완료, 현재 잔액: {계좌 잔액(숫자 3개마다 ','을 표기해서)원}'으로 출력해라

    except ValueError:      #try해서 value에서 error가 생긴다면,
        print('[금액만] 다시 입력하세요.')      #'금액만을 입력해라'는 메세지를 출력해라
        return              #되돌아가라


def subMoney():                 #함수: sub한다, money를
    global accountBalance       #전역변수 accountBalance를 지역변수로서 사용 가능하도록
    try:        #시도해라
        minus = int(input('금액을 입력하세요, 출금 금액: '))    #'빼기'는 input되어 int로 캐스팅된 '출금할 금액'이다
        if minus <= 0:           #만약에, '빼기'가 0보다 작거나 같다면 ->//
            print('0원 이하 금액은 출금할 수 없습니다.')        #//-> '출금이 불가하다'는 메세지를 출력해라
            return              #되돌아가라
        
        elif minus > accountBalance:    #2번 만약에, '빼기'가 계좌 잔액보다 크다면,
            print('출금 금액이 계좌 잔액보다 많습니다.')        #'출금하려는 금액이 잔액보다 많다'는 메세지를 출력해라
            return              #되돌아가라
            
        elif minus <= accountBalance:    #3번 만약에, '빼기'가 계좌 잔액보다 작거나 같다면,
            print('출금 중입니다.')     #'출금 중'이라는 메세지를 출력해라
            accountBalance -= minus     #'계좌 잔액'에서 '빼기'의 값(출금할 금액)를 빼라
            now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            #'지금'은 '(모듈)날짜.지금날짜.지금()'을 문자열로 바꿔라, 
            # '%Y-%m-%d %H-%M-%S(2026-05-28 22-22-16)'의 형식으로
            backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG].append(
                #(파일)은행계좌 데이터베이스.(딕셔너리)은행계좌 데이터베이스.[(모듈)은행 계좌번호]
                # [(모듈)은행 계좌번호][(모듈)은행 계좌기록]에 추가해라,
                (now, minus, '출금')
                #'지금시각, 빼기(출금 금액), "출금"'의 양식대로 입금 데이터를
            )
            print(f'출금 완료, 현재 잔액: {accountBalance:,}원')
            #'출금 완료, 현재 잔액: {계좌 잔액(숫자 3개마다 ','을 표기해서)원}'으로 출력해라

    except ValueError:      #try해서 value에서 error가 생긴다면,
        print('[금액만] 다시 입력하세요.')      #'금액만을 입력해라'는 메세지를 출력해라
        return               #되돌아가라


def moneyFlow():        #함수: money의 flow(흐름)은
    global accountBalance       #전역변수 accountBalance를 지역변수로서 사용 가능하도록
    myMoneyFlow = backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG]
    #'나의 money의 flow'에 (파일)은행계좌 데이터베이스.(딕셔너리)은행계좌 데이터베이스.[(모듈)은행 계좌번호]
    # [(모듈)은행 계좌번호][(모듈)은행 계좌기록]을 할당한다
    deepcopieFlow = copy.deepcopy(myMoneyFlow)      #'깊은복사한 flow'에 (모듈)복사.깊은복사(나의 money의 flow(를 매개변수로))
    deepcopieFlow.reverse()                         #'깊은복사한 flow'를 reverse(내림차순)해라
    now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    #'지금'은 '(모듈)날짜.지금날짜.지금()'을 문자열로 바꿔라, 
    # '%Y-%m-%d %H-%M-%S(2026-05-28 22-22-16)'의 형식으로
    print(f'\n조회 일시: {now}')        #'조회 일시: {지금}'라는 메세지를 출력해라
    if len(deepcopieFlow) == 0:        #만약에, '깊은복사한 flow'에 할당된 데이터 길이(len)가 '0'이라면, 
        print('거래내역이 없습니다.')       #'거래내역이 없다'라는 메세지를 출력해라
        return                     #되돌아가라        
    
    else:       #만약이 아니라면,
        for idx, flow in enumerate(deepcopieFlow):  #반복문: 인덱스 번호, '흐름'의 데이터를 쌍으로서 생성한다
            date, money, kind = flow                #'흐름'이라는 데이터에는 '날짜', '금액', '기록'가 속해있다
            print(f'[{date} / {idx+1}] {kind} {money:,}원')
            #f'[{날짜} / {인덱스 번호(+1)}] {기록} {금액(숫자 3개마다 ','을 표기해서)원}'으로 출력헤라


def saveJson():     #함수: save해라, json형식의 파일을
    now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    #'지금'은 '(모듈)날짜.지금날짜.지금()'을 문자열로 바꿔라, 
    # '%Y-%m-%d %H-%M-%S(2026-05-28 22-22-16)'의 형식으로
    fileName = f'{now}_balance_data.json'       #'파일이름'은 '{지금}_balance_data.json'이다
    history = backAccountDb.bankAccountDb[config.BANK_ACNT][config.BANK_ACNT][config.BANK_LOG]
    #'역사'에 (파일)은행계좌 데이터베이스.(딕셔너리)은행계좌 데이터베이스.[(모듈)은행 계좌번호]
    # [(모듈)은행 계좌번호][(모듈)은행 계좌기록]을 할당한다
    save_data = {       #'save한다, data를'는 : {딕셔너리}
        "account_number": config.BANK_ACNT,     #'계좌 번호'에는 '(모듈)은행 계좌번호'이 할당된다
        "current_balance": accountBalance,      #'현재 잔액'에는 '계좌 잔액'이 할당된다
        "transaction_history": history          #'거래 내역'에는 '역사'가 할당된다
        }

    with open(fileName, 'w', encoding='utf8') as f:     #함께, open해라('파일이름', 'write', 한글깨짐 방지 코드)는 같다, f와
        jsonFile = json.dumps(save_data, indent=4, sort_keys=True, ensure_ascii=False)
        #json파일은 (모듈)json.'한번에 담는다'('save한다, data를', 4칸 들여쓰고, 딕셔너리 key는 알파벳 순서로, 
        # 한글은 깨지지 않게 그대로)
        f.write(jsonFile)       #'f'를 write해라(json파일을 매개변수로서)
    

def setMoneyFlow():     #함수: set한다, money의 flow를
    global flag       #전역변수 flag를 지역변수로서 사용 가능하도록
    while flag:         #flag변수가 True일때 동안에
        try:        #시도해라
            inputData = int(input('메뉴를 선택하세요, 1.입금    2.출금    3.내역    99.종료'))
            #'입력받은 데이터'는 input되어 int로 캐스팅된 '메뉴 선택'이다
            if inputData == ADD_MONEY:      #만약에, '입력받은 데이터'가 '1.입금'일때
                addMoney()      #함수: 'add한다, money를'를 실행해라
                saveJson()      #함수: 'save해라, json형식의 파일을'를 실행해라

            elif inputData == SUB_MONEY:    #2번 만약에, '입력받은 데이터'가 '2.출금'일때
                subMoney()      #함수: 'sub한다, money를'를 실행해라
                saveJson()      #함수: 'save해라, json형식의 파일을'를 실행해라

            elif inputData == MONEY_FLOW:   #3번 만약에, '입력받은 데이터'가 '3.내역'일때
                moneyFlow()     #함수: 'money의 flow(흐름)은'를 실행해라

            elif inputData == SELECT_END:   #4번 만약에, '입력받은 데이터'가 '99.종료'일때
                print('종료합니다.')    #'종료'라는 메세지를 출력해라
                flag = False    #flag(깃발)변수 = False(거짓)으로 재할당
            
            else:       #만약이 아니라면,
                print('잘못된 메뉴선택입니다.')     #'잘못된 메뉴선택'이라는 메세지를 출력해라

        except ValueError:      #try해서 value에서 error가 생긴다면,
            print('[올바른] 메뉴를 선택하세요.')    #'올바른 메뉴를 선택해라'라는 메세지를 출력해라
            return      #되돌아가라

