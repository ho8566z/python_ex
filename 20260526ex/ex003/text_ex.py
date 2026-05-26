# 텍스트 파일 다루기
# 문자열의 영구적으로 보관하기 위함

# 1단계: 파일 열기
# 파일을 여는 단계, 'open()' 함수를 이용한다(파일 외 ex: 데이터 베이스 등등)
# 파일 열기에 성공하면, 파일은 객체로 만들어져 메모리에 생성된다

# 2단계: 파일 쓰기/읽기
# 문자열을 쓰거나 읽음, 문자열을 쓸때는 'write()' 함수를, 읽을 때는 'read()' 함수를 이용한다

# 3단계: 파일 닫기
# 파일을 닫는 단계로, 쓰거나 읽기가 끝난 파일은 'close()' 함수를 이용해 닫는다



# file = open('C:/lyh/python/test.txt', 'w')      # 파일을 '쓰기'모드로 open한다
# # open('C:/lyh/python: 원하는 설치 경로/test.txt: 파일명', 'w: 파일 목적'): open()함수
# result = file.write('Hello, Python.')           # 쓰기(write)
# print(f'result: {result}')                      # 쓰여진 문자열의 길이
# file.close()                                    # 파일 닫기(close, 외부자원 해제)



# file = open('C:/lyh/python/test.txt', 'r')
# readResult = file.read()
# print(f'readResult: {readResult}')                # readResult: Hello, Python.

# # C:/lyh/python/test.txt <-- '100' 입력
# print(f'readResult: {readResult}')                # readResult: 100
# print(f'readResult type: {type(readResult)}')     # readResult type: <class 'str'>

# readResult = int(readResult)
# readResult += 1
# print(f'readResult: {readResult}')                # readResult: 101

# file.close



# file = open('C:/lyh/python/test.txt', 
# 'w: write((새로이)쓰기) / a: append(추가로 쓰기) / r: read(읽기)')

# file = open('C:/lyh/python/test.txt', 'w')
# file.write('hello.')
# file.close()

# with open('C:/lyh/python/test.txt', 'w') as file:
#     file.write('hello.')

# file = open('C:/lyh/python/test.txt', 'a')
# file.write('\nhi.')
# file.close()

# with open('C:/lyh/python/test.txt', 'a') as file:
#     for n in range(10):
#         file.write('\nhello.')      
# # close는 'with ~ as'구문을 쓰면, 알아서 적용됨

# file = open('C:/lyh/python/test.txt', 'r')
# readResult = file.read()
# print(f'readResult: {readResult}')   
# file.close()
# # readResult: hello.
# # hi.



# # 예외 처리(보험)
# # 세상에 모든 프로그램은 100% 완벽할 수 없다, 때문에 -> '보험'

# print(10 + 20)      #30
# print(10 - 20)      #-10
# print(10 * 20)      #200
# print(10 / 20)      #0.5


# print(10 + 20)      #30
# print(10 / 0)       #ZeroDivisionError: division by zero
# print(10 - 20)      #출력(x)
# print(10 * 20)      #출력(x)



# # 예외 처리의 기본 문법
# '''
# try ~ except
# '''

# print(10 + 20)      #30
# try:
#     print(10 / 0)   #출력(x): 에러가 발생하더라도, 넘어감
# except Exception as e:
#     print(f'Exception: {e}')    #Exception: division by zero
# else:
#     print('에러가 발생하지 않았다')     #try와 반대의 결과 도출
# finally:
#     print('에러가 발생하든, 하지않든 무조건 실행되는 코드')

# print(10 - 20)      #-10
# print(10 * 20)      #200


# # try ~ except에 많은 코드를 넣으면, 오류가 발생한 다음의 정상적인 
# # 코드들은 실행되지 않는다
# try:
#     print(10 + 20)      #30
#     print(10 / 0)       #출력(x): 에러가 발생하더라도, 넘어감
#     print(10 - 20)      #-10
#     print(10 * 20)      #200
# except Exception as e:
#     print(f'Exception: {e}')    #Exception: division by zero


