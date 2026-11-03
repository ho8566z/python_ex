import config
from util import getDay, getTime


# dFlag 가 False 가 되면 반복문이 끝나 프로그램이 종료된다
dFlag = True

while dFlag:
    selectedMenuNum = int(input('메뉴: 1.일기작성    2.일기조회    99종료'))

    if selectedMenuNum == config.DIARY_WRITE:

        print(f'[{getDay()}] 한줄 일기를 작성하세요.')

        todayDiary = input()
        # 'a' 모드는 기존 일기 뒤에 이어서 쓴다
        with open('C:/lyh/python/diary.txt', 'a') as f:
            f.write(f'[{getDay()} {getTime()}] {todayDiary}\n')

    elif selectedMenuNum == config.DIARY_READ:
        
        # 'r' 모드로 저장된 일기 전체를 읽어 출력한다
        with open('C:/lyh/python/diary.txt', 'r') as f:
            str = f.read()
            print(str)

    elif selectedMenuNum == config.SYSTEM_SHUTDPWN:
        print('end')
        dFlag = False
