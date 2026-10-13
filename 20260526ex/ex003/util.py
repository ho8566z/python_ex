import time

# 오늘 날짜를 'YYYY-MM-DD' 문자열로 돌려준다.
def getDay():
    return time.strftime('%Y-%m-%d', time.localtime())

# 현재 시각을 'HH:MM:SS' 문자열로 돌려준다.
def getTime():
    return time.strftime('%H:%M:%S', time.localtime())
