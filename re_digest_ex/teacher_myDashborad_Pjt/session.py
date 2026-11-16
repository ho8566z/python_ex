signInedMemberId = '001'

# setter
def setSignInedMemberId(mId=''):
    '''로그인한 회원의 ID를 세션에 저장한다. 빈 문자열이면 로그아웃 상태가 된다.'''
    global signInedMemberId
    signInedMemberId = mId

# getter
def getSignInedMemberId():
    '''세션에 저장된 로그인 회원의 ID를 반환한다.'''
    return signInedMemberId