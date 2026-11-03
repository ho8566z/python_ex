from db import member_db
from db import diary_db

# 개발용 더미 회원 정보: 같은 인덱스끼리 한 회원이다
ids = ['gildong', 'chanho', '001']
pws = ['1234', '5678', '002']
mails = ['gildong@gmail.com', 'chanho@naver.com', '003']
phones = ['010-0001-0002', '010-0011-0022', '004']


def dumyInit():
    # 더미 회원을 회원 DB 에 넣고, 회원마다 빈 일기 목록을 만든다
    for n in range(len(ids)):
        member_db.memberDB[ids[n]] = {
            'uId': ids[n],
            'uPw': pws[n],
            'uMail': mails[n],
            'uPhone':phones[n]
        }

        diary_db.diaryDB[ids[n]] = []
