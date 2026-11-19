'''module02: import 될 때도 fun() 이 바로 실행되는 모듈.'''
# import 되면 모듈 이름이, 직접 실행하면 '__main__' 이 __name__ 에 담긴다.
def fun():
    '''module02 의 함수가 실행됐음을 출력한다.'''
    print('module02의 함수 실행')

fun()

print(f'module02의 __name__: {__name__}')
