from datetime import datetime

# 현재 시각을 'YYYY-MM-DD HH:MM:SS' 문자열로 돌려준다.
def getCurrentDateTime():
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')