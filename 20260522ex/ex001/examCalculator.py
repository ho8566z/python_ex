# 두 수를 받아 사칙연산 결과를 출력하는 계산기 함수 모음
def addition(n1, n2):
    '''두 수를 더한 결과를 출력한다.'''
    print(f'덧셈: {n1 + n2}')

def subtraction(n1, n2):
    '''첫 번째 수에서 두 번째 수를 뺀 결과를 출력한다.'''
    print(f'뺄셈: {n1 - n2}')

def multiplication(n1, n2):
    '''두 수를 곱한 결과를 출력한다.'''
    print(f'곱셈: {n1 * n2}')

def division(n1, n2):
    '''첫 번째 수를 두 번째 수로 나눈 결과를 출력한다.'''
    print(f'나눗셈: {n1 / n2}')

def rest(n1, n2):
    '''나머지(%)를 출력한다.'''
    print(f'나머지: {n1 % n2}')

def portion(n1, n2):
    '''몫(//)을 출력한다. 나눗셈(/)과 달리 소수점 아래를 버린다.'''
    print(f'몫: {n1 // n2}')

