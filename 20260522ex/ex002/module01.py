def fun():
    print('module01의 함수 실행')

# fun()

# print(f'module01의 __name__: {__name__}')

if __name__ == '__main__':
    fun()

# 해당: module01.py 파일이 실행 파일일때, 해당 파일의 타입은 __main__이 되면서
# 해당 명령이 실행되지만, 다른 파일에서 실행한다면, 위의 명령은 실행되지 않는다.

