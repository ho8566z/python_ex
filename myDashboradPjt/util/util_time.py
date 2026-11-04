from datetime import datetime

# 현재 시각을 'YYYY-MM-DD HH:MM:SS' 문자열로 돌려준다.
def getCurrentDateTime():
    '''현재 날짜와 시각을 'YYYY-MM-DD HH:MM:SS' 형식의 문자열로 반환한다.'''
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')