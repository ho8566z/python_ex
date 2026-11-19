'''module01: 직접 실행할 때만 fun() 을 호출하는 모듈.'''

def fun():
    '''module01 의 함수가 실행됐음을 출력한다.'''
    print('module01의 함수 실행')

# fun()

# print(f'module01의 __name__: {__name__}')

if __name__ == '__main__':
    fun()

# 해당: module01.py 파일이 실행 파일일때, 해당 파일의 타입은 __main__이 되면서
# 해당 명령이 실행되지만, 다른 파일에서 실행한다면, 위의 명령은 실행되지 않는다.

