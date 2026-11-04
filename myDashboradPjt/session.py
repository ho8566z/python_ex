signInedMemberId = ''

# setter
def setSignInedMemberId(mId=''):
    """로그인한 회원ID를 저장한다. 인자를 생략하면 빈 문자열이 되어 로그아웃 상태가 된다."""
    global signInedMemberId
    signInedMemberId = mId

# getter
def getSignInedMemberId():
    """현재 로그인한 회원ID를 반환한다. 로그인 전에는 빈 문자열이다."""
    return signInedMemberId