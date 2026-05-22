import module01
import module02
import module03

# print('this is 실행파일')
# # module01의 함수 실행
# # module02의 함수 실행
# # module03의 함수 실행
# # this is 실행파일


# ex)
# print(f'app:실행파일의 __name__: {__name__}')
# # module01의 함수 실행
# # module01의 __name__: module01     #해당 모듈명
# # module02의 함수 실행
# # module02의 __name__: module02
# # module03의 함수 실행
# # module03의 __name__: module03
# # this is 실행파일
# # app:실행파일의 __name__: __main__     #구분: main 파일



# if __name__ == '__main__':
#     fun()

# ex2)
print(f'app:실행파일의 __name__: {__name__}')
# module02의 함수 실행
# module02의 __name__: module02
# module03의 함수 실행
# module03의 __name__: module03
# app:실행파일의 __name__: __main__
