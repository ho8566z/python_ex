import os       #현재 실행 중인 파이썬 파일의 절대 경로를 가져온다
import sys      #위에서 얻은 파일 경로에서 파일 이름을 제외한 폴더 경로를 추출한다

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#현재 파일이 위치한 폴더의 상위 폴더 경로를 파이썬 모듈 검색 경로에 추가하여, 상위 폴더 내의 모듈을 불러올 수 있게 만듦

from memberService import session           #로그인 상태를 검증하는 모듈 파일을 소환(import)한다
from memberService import memberService     #'memberService'디렉토리에서 'memberService'모듈을 소환x
import datetime     #날짜 및 시간을 확인 가능한 모듈을 소환
import copy         #데이터를 복사할 수 있는 모듈을 소환
import json         #json형식으로 파일을 관리가능한 모듈을 소환x
from memberService import session           #'memberService'디렉토리에서 'session'모듈을 소환(로그인 상채, 확인을 위해)
from db import config       #'db'디렉토리에서 'config(상수)'모듈을 소환
from db import dbManager    #'db'디렉토리에서 'dbManager(함수)'모듈을 소환

ADD_SUB_MONEY = 1       #상수: 입금 및 출금 = '1'로 할당
MONEY_FLOW = 2          #상수: 입출 내역 = '2'로 할당
SELECT_END = 99         #상수: 입출메뉴 종료 = '99'로 할당

flag = True             #flag(깃발)변수 = True(참)으로 할당
accountBalance = 0      #'계좌 잔액' 데이터에 입출 내역에 따라 데이터를 기록하기 전에 '0'으로 할당


def fastBalance():          #함수: fast(과거의), balance(잔액) = 과거의 잔액을 확인하는
    global accountBalance   #전역변수 accountBalance를 지역변수로서 사용 가능하도록
    accountBalance = 0      #'계좌 잔액' 데이터에 입출 내역에 따라 데이터를 기록하기 전에 '0'으로 할당
    accountNumber = dbManager.members[session.signinedId]["BANK_ACNT"]
    #변수명: '계좌번호'에, 모듈: dbManager의 members(회원들)에서 'session.signinedId(로그인 상태일때), 
    # "BANK_ACNT(은행 계좌번호)"의 값을 할당한다'

    balanceLogs = dbManager.bankAccounts[accountNumber].get(config.BANK_LOG, [])
    #변수명: '잔액 기록들'에, 모듈: dbManager의 members(회원들)에서 [accountNumber(계좌번호)]에서 
    # get한다, 모듈:'config의 BANK_LOG(은행 내역)의 밸류값인 []리스트'를 할당한다
    for log in balanceLogs:     #'balanceLogs'의 속한, 'log'를 꺼내 반복문을 실행한다
        _, amount, kind = log   
        #'log'가 가진 데이터 '날짜', '금액', '(입금/출금)종류'들을 첫번째 값인 '날짜'를 
        # 제외하고, 'amount(<=금액)', 'kind(<=종류)'를 구조분해 할당으로 저장한다
        if kind == "입금":       #만약에, 거래종류가 '입금'이라면,
            accountBalance += amount    #'계좌잔액'에 '금액'을 더한다 
        else:       #만약이 아니라면,
            accountBalance -= amount    #'계좌잔액'에서 '금액'을 뺀다


def setBankAccount(id):     #함수: set(설정)힌다, bank(은행)의 account(계좌)를 = 은행계좌를 설정히는 함수
    inputAccountPw = input("계좌 비밀번호 입력: ")
    #변수명: '입력받은 계좌 비밀번호'에, '계좌번호 비밀번호'를 입력받아 할당한다
    
    if inputAccountPw.isdigit():        #만약에, '입력받은 계좌 비밀번호'가 '정수'인지 검증한다(내장함수를 통해)
        print("계좌 비밀번호가 설정되었습니다.")    #'계좌 비말번호가 설정되었다'라는 메세지를 출력해라
    else:       #만약이 아니라면,
        print("비밀번호를 다시 입력하세요.")        #비밀번호를 재입력하라'라는 메세지를 출력해라

    dbManager.createBankAccount(id, inputAccountPw)     
    #모듈: dbManager의 created(만든다) bank(은행)의 account(계좌)를 = 은행계좌을 만드는 함수이다
    # 'id(회원id)와 inputAccountPw(입력받은 계좌 비밀번호)' 데이터를 매개변수로서
    accountNumber = dbManager.members[id]["BANK_ACNT"]
    #변수명: '계좌번호'에, 모듈: dbManager의 members(회원들)에서 [(회원)id]와 [BANK_ACNT(은행 계좌번호)]의 값을 할당한다
    print(f"Bank_Account created: {accountNumber}")
    #'은행 계좌를 만들었고, 계좌번호는 [(만들어진)계좌번호]이다'라는 메세지를 출력해라


def calculateMoney(kind):           #함수: calculate(계산)한다, money(돈)을
    global accountBalance   #전역변수 accountBalance를 지역변수로서 사용 가능하도록
    inputMoney = input(f"입금 및 출금할 금액을 입력하세요: ")
    #'입력받은 금액'에 '입금 및 출금할 금액'를 입력받아 할당한다

    if not inputMoney.isdigit():        #만약에, '입력받은 금액'가 '정수'인지 검증해 '아닌' 경우에는(내장함수를 통해)
        print("금액을 다시 입력하세요.")    #'금액을 다시 입력해라'라는 메세지를 출력해라
        return None     #'어떠한 결과값도 가지지 않고' 되돌아가라

    intMoney = int(inputMoney)          #변수명: '정수 형의 금액'에, '입력받은 금액'을 int로 캐스팅해 할당한다
    if intMoney <= 0:   #만약에, '정수 형의 금액'보다 '0'이 크거나 같을때,
        print("0원 미만은 입금 및 출금할 수 없습니다.")     #'0원 미만은 입금 및 출금할 수 없다'라고 메세지를 출력해라
        return None     #'어떠한 결과값도 가지지 않고' 되돌아가라

    if kind == "입금":   #1번째 만약에, (입/출)종류가 '입금'인 경우에
        accountBalance += intMoney      #'계좌잔액'에 '정수 형의 금액'을 더해라
    elif kind == "출금":    #1번째, 2번 만약에, (입/출)종류가 '출금'인 경우에
        if accountBalance < intMoney:   #2번째 만약에, '계좌잔액'이 '정수 형의 금액'보다 적을때
            print("잔액이 부족합니다.")    #'잔액이 부족하다'라는 메세지를 출력해라
            return None     #'어떠한 결과값도 가지지 않고' 되돌아가라
        accountBalance -= intMoney      #'계좌잔액'에서 '정수 형의 금액'을 빼라

    print(f"입금 및 출금 완료, 현재 잔액: {accountBalance}")
    #'입금 및 출금이 완료되었고, 현재 잔액은 "계좌잔액"이다'라는 메세지를 출력해라
    return intMoney     #'정수 형의 금액'의 값을 가지고 되돌아가라


def moneyFlow():        #함수명: money(돈)의 flow(흐름)
    global accountBalance   #전역변수 accountBalance를 지역변수로서 사용 가능하도록
    accountNumber = dbManager.members[session.signinedId]["BANK_ACNT"]
    #변수명: '계좌번호'에, 모듈: dbManager의 members(회원들)에서 'session.signinedId(로그인 상태일때), 
    # "BANK_ACNT(은행 계좌번호)"의 값을 할당한다'

    userDonggeun = dbManager.bankAccounts.get(accountNumber)
    #변수명: '이스터에그'에, '모듈: dbManager의 bank(은행)accounts(계좌목록)에서 
    # accountNumber(계좌번호)'를 매개변수로서 get한 값을 할당한다
    myMoneyFlow = userDonggeun.get(config.BANK_LOG)
    #변수명: '나의 돈의 흐름'에, '이스터에그'에 '모듈: config의 BANK_LOG(은행 기록)'을 get한 값을 할당한다

    if not myMoneyFlow:     #만약에, '나의 돈의 흐름'이 '0'이나 'None'이 아닌 경우에만,
        print("거래내역이 없습니다.")   #'거래내역이 없다'라는 메세지를 출력해라
        return      #되돌아가라

    deepcopieFlow = copy.deepcopy(myMoneyFlow)
    #변수명: '깊은복사한 흐름'에, 모듈 copy의 deepcopy을 통해 '나의 돈의 흐름'을 매개변수로서 깊은 복사해 할당한다
    deepcopieFlow.reverse()     #'깊은복사한 흐름'을 '모듈: reverse'를 이용해 내림차순으로 변경해라

    now = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    #변수명: '지금'에, 모듈: datetime의 datetime(날짜와 시간)에서 'now(현재)'를 
    # '%Y-%m-%d %H-%M-%S'형식의 문자열로 바꿔서 할당한다
    print(f"\n조회 일시: {now}")        #'조회일시는 "지금"이다'라는 메세지를 출력해라

    for idx, flow in enumerate(deepcopieFlow):      #'인덱스 번호'와 '흐름'을 '동시'에 가져오는 동안에
        date, money, kind = flow        #'시간', '돈', '(입/출)종류'를 '흐름'에서 구조분해하여 할당한다
        print(f"[{date} / {idx+1}] {kind} {money}원 / 잔액 {accountBalance}원")
        #'["시간" / "인덱스 번호(+1)""] "(입/출)종류" "돈'원 / 잔액 "계좌잔액"원'이라는 메세지를 출력해라


def setMoneyFlow():     #함수: set한다, money의 flow를 = '돈의 흐름을 선택한다'
    global flag         #전역변수 flag를 지역변수로서 사용 가능하도록
    while flag:         #flag변수가 True인 동안, while(반복)한다
        inputData = input("메뉴를 선택하세요, 1.입금 및 출금    2.내역    99.종료")
        #(1.입금 및 출금    2.내역    99.종료, 중에서)'입력받은 데이터'는 input된 '메뉴 선택'이다
        if inputData.isdigit():             #1번째 만약에, '입력받은 데이터'가 '정수'인지 검증한다(내장함수를 통해)
            selected1 = int(inputData)      #변수명: '선택1'에, '입력받은 데이터'를 int로 캐스팅해 할당한다
            if selected1 == ADD_SUB_MONEY:  #2번째 만약에, '선택1'이 '1.상수: 입금 및 출금'일때
                selected2 = input("1.입금    2.출금")
                #변수명: '선택2'에, ("1.입금    2.출금") 중에 하나를 선택해 할당한다
                kind = "입금" if selected2 == "1" else "출금"   
                #종류(가) = '입금'일때는, 만약에 '선택2'가 '1번'인 경우이다, 만약이 아니라면, '출금'이다
                amount = calculateMoney(kind)   
                #변수명: amount(:금액)는, '함수: calculate(계산)한다, money(돈)을' 함수(의 '종류'를 매개변수로)를 할당한다
                if amount:      #3번째 만약에, 'amount(금액)'이 '0'이나 'None'이 아닌 경우에만,
                    dbManager.createdFlowHistory(session.signinedId, amount, kind)
                    #모듈: dbManager의 created(만든다) flow(흐름)의 history(역사)를 = 거래내역을 만드는 함수이다
                    # 'session.signinedId(로그인 상태일때), amount(금액), kind(종류)' 등의 데이터를 통해서
                    print(f"[{kind}] 처리가 완료되었습니다.")   
                    #'(입금 및 출금에 해당하는)종류의 처리가 완료되었다'라는 메세지를 출력해라

            elif selected1 == MONEY_FLOW:       #2번째, 2번 만약에, '선택1'이 '2.내역'일때
                moneyFlow()     #money(돈)의 flow(흐름)라는 함수를 실행한다

            elif selected1 == SELECT_END:       #2번째, 3번 만약에, '선택1'이 '99.종료'일때
                print("종료합니다.")    #'종료한다'라는 메세지를 출력해라
                flag = False    #'flag' 변수를 'False'로 재할당해 다시 반복문을 중단한다

            else:               #2번째 만약이 아니라면,
                print("잘못된 메뉴선택입니다.")     #'잘못된 메뉴선택'이라는 메세지를 출력해라

        else:           #1번째 만약이 아니라면,
            print("[올바른] 메뉴를 선택하세요.")    #'올바른 메뉴를 선택하라'이라는 메세지를 출력해라
            return      #되돌아가라


def startLoop():                #함수: start한다, loop(루프)를
    global flag                 #전역변수 flag를 지역변수로서 사용 가능하도록

    if session.onSignIned():    #만약에, 로그인 상태를 확인했을 때, 로그인 중이라면,
        fastBalance()           #함수: fast(과거의), balance(잔액) = 과거의 잔액을 확인하는 함수를 실행한다
        setMoneyFlow()          #'set한다, money의 flow를' 함수를 실행한다

    else:                       #만약이 아니라면,
        print("로그인을 진행한 다음, 진행하세요.")  #'로그인이 우선이라는 메세지'를 출력해라
        return                  #되돌아가라

    flag = True                 #'flag' 변수를 'True'로 재할당해 다시 반복문을 반복한다
