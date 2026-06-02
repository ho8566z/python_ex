from db.memberAccountDb import memberAccountDb as members
from db.backAccountDb import bankAccountDb as bankAccounts
from db.memoDb import memoDb as memos
from db.todoListDb import todoListDb as todoLists
from db import config

import datetime


# ------ member ------
def createMember(id, pw, mail, phone):
    members[id] = {
        config.ID: id,
        config.PW: pw,
        config.MAIL: mail,
        config.PHONE: phone,
        config.BANK_ACNT: None,     
        #모듈: 'memberService'의 함수: signUp에서 input받지 않았던 것처럼, 
        # 'BANK_ACNT'는 'None'에 해당하는 어떠한 결과값도 가지지 않는다
    }

    memos[id] = []
    todoLists[id] = []


def getMemberIds():
    return members.keys()


def getMemberPw(id):
    return members[id][config.PW]


# ------ bank ------
def getMemberBankAcnt(id):      
    #함수명: 'get한다, member(회원의) bank(은행) acnt(계좌)를'
    return members[id][config.BANK_ACNT]    
    #members(회원목록)을 [id]와 [모듈 connfig의 BANK_ACNT(은행_계좌)]를 통해서


def createBankAccount(id, pw):
    #함수명: 'create(만든다), bank(은행) account(계좌)를' 
    #= 은행 계좌를 만드는 함수를 회원id와 pw를 매개변수로서 실행한다 ->//
    #//-> 함수: created(만든다) flow(흐름)의 history(역사)를 (id, pw데이터를 매개변수로서)
    if id not in members:           #만약에, 'id'가 'member(회원목록)'에 있지 않을때
        print(f'회원 없음: {id}')     #'[id]에 해당하는 회원은 없다'라는 메세지를 출력해라
        return      #되돌아가라
    
    accountCode = f"101-77-{id}"    #변수명: '계정 번호'는, f'(양식)101-77-'을 할당한다

    bankAccounts[accountCode] = {   #'은행 계좌목록'은 [계정 번호]를 통해
        config.BANK_PW: pw,         #[은행_비밀번호]는 사용자에게 입력빋은 'pw'이다
        config.BANK_LOG: [],        #[은핼_기록]은 사용자가 지금까지 이용한 []리스트이다
    }

    members[id][config.BANK_ACNT] = accountCode
    #members(회원목록)의 [id]에 [모듈: config에 "은행_계좌"]에 '계정 번호'를 할당한다

def createdFlowHistory(id, inputMoney, kind):       
    #함수명: 'created(만든다), flow(흐름) history(역사를)'에 'id(회원id)', 
    # 'inputMoney(입력받은 금액)', 'kind(입/출 종류)'를 매개변수로서 데이터를 받는다
    if members[id][config.BANK_ACNT] not in bankAccounts:
    #만약에, members(회원목록)에 [id], [모듈: comfig의 은행_계좌]에서 '은행 계좌목록'이 없는 경우에만,
        return      #되돌아가라
    
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #변수명: '시간'에, 모듈: datetime의 datetime(날짜와 시간)에서 'now(현재)'를 
    # '%Y-%m-%d %H-%M-%S'형식의 문자열로 바꿔서 할당한다
    history = (time, inputMoney, kind)
    #변수명: '역사'에 튜플 데이터인 '시간', '입력받은 금액', '입/출 종류'를 할당한다
    bankAccounts[members[id][config.BANK_ACNT]][config.BANK_LOG].append(history)
    #'은행 계좌목록'의 [members(회원목록)의[id], [모듈: config의 BANK_ACNT(은행_계좌)], 
    # 그리고[모듈: BANK_LOG(은행 기록)]]에 추가한다, ('역사')를


# ------ memo ------
def getMemoList(id):
    return memos[id]


def hasMemo(id):
    return id in memos and len(memos[id]) > 0

def createMemo(id, text):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    memo = {config.MEMO_DATE: time, config.MEMO_TEXT: text}

    memos[id].append(memo)

def updateMemo(id, num, newText):
    memos[id][num][config.MEMO_TEXT] = newText
    memos[id][num][config.MEMO_DATE] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def deleteMemo(id, num):
    del memos[id][num]

    
# ------ todolist ------
def createTodo(id, workNote, finishDay):
    now = datetime.datetime.now()
    expired_time = now + datetime.timedelta(days=finishDay)

    inforMationBox = {
        config.TODO_TEXT: workNote,
        config.REGISTER_DAY: now.strftime("%Y-%m-%d %H:%M:%S"),
        config.EXPIRED_DAY: expired_time.strftime("%Y-%m-%d %H:%M:%S"),
        config.REMAINING: str(finishDay),
        config.SUCCESS: False,
    }

    todoLists[id].append(inforMationBox)
