from db import member_db
from db import diary_db

ids = ['gildong', 'chanho']
pws = ['1234', '5678']
mails = ['gildong@gmail.com', 'chanho@naver.com']
phones = ['010-0001-0002', '010-0011-0022']


def dumyInit():
    for n in range(len(ids)):
        member_db.memberDB[ids[n]] = {
            'uId': ids[n],
            'uPw': pws[n],
            'uMail': mails[n],
            'uPhone':phones[n]
        }

        diary_db.diaryDB[ids[n]] = []
