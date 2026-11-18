from memberService import session
from memberService import memberService
from bankAccount import bankAccount
from memoService import memo
from ToDoList import todolist
from db import fileManager

OPT_EXIT = "0"
OPT_SIGN_UP = "1"
OPT_SIGN_IN = "2"
OPT_SIGN_OUT = "3"
OPT_MODIFY = "4"
OPT_BANK = "5"          #옵션_은행(서비스)는 '5'이다
OPT_MEMO = "6"
OPT_TODO = "7"

onRunning = True


def exit():
    '''반복을 멈추도록 표시하고 모든 데이터를 파일에 저장한다.'''
    global onRunning
    onRunning = False
    fileManager.dbSaveAllAtFile()


def notImplemented():
    '''아직 구현되지 않은 메뉴임을 알린다.'''
    print("아직 구현되지 않은 기능입니다.")


signInedActions = {
    OPT_SIGN_OUT: memberService.signOut,
    OPT_MODIFY: notImplemented,
    OPT_BANK: bankAccount.startLoop,        #옵션_은행(서비스)가 선택되면, '함수: start한다, loop(루프)를'이 실행된다
    OPT_MEMO: memo.memoLoop,
    OPT_TODO: todolist.startLoop,
}

signOutActions = {
    OPT_EXIT: exit,
    OPT_SIGN_UP: memberService.signUp,
    OPT_SIGN_IN: memberService.signIn,
}


def makePromptAndActions(onSignedIn):
    '''로그인 여부에 맞는 메뉴 문구와 (번호 → 실행 함수) 딕셔너리를 만들어 돌려준다.'''
    text = ""
    actions = {}

    if onSignedIn:
        text = (
            f"{OPT_SIGN_OUT}. 로그아웃 "
            f"| {OPT_MODIFY}. 회원 정보 수정 "
            f"| {OPT_BANK}. 계좌 "
            f"| {OPT_MEMO}. 메모 "
            f"| {OPT_TODO}. 투두리스트 "
        )
        actions = signInedActions

    else:
        text = (
            f"{OPT_SIGN_UP}. 회원가입 "
            f"| {OPT_SIGN_IN}. 로그인 "
            f"| {OPT_EXIT}. 종료 "
        )
        actions = signOutActions

    return (text, actions)


def main():
    '''파일에서 데이터를 불러온 뒤 종료할 때까지 메뉴를 반복하고, 끝나면 저장한다.'''
    fileManager.dbLoadAllFromFile()

    while onRunning:
        prompt, actions = makePromptAndActions(session.onSignIned())
        selected = input(f"\n{prompt}\n:")

        action = actions.get(selected)
        action() if action else None

    fileManager.dbSaveAllAtFile()
    
if __name__ == "__main__":
    from db import fileManager

    main()
