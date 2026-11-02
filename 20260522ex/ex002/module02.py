# import 되면 모듈 이름이, 직접 실행하면 '__main__' 이 __name__ 에 담긴다.
def fun():
    print('module02의 함수 실행')

fun()

print(f'module02의 __name__: {__name__}')
