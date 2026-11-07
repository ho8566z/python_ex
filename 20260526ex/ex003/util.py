import time

def getDay():
    '''오늘 날짜를 'YYYY-MM-DD' 문자열로 돌려준다.'''
    return time.strftime('%Y-%m-%d', time.localtime())

def getTime():
    '''현재 시각을 'HH:MM:SS' 문자열로 돌려준다.'''
    return time.strftime('%H:%M:%S', time.localtime())
