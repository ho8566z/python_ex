# 모듈명 단축하기: as

# import examCalculator as ca

# # examCalculator.addition(10, 20)
# # examCalculator.subtraction(20, 10)
# # examCalculator.multiplication(10, 10)
# # examCalculator.division(100, 10)
# # examCalculator.rest(100, 30)
# # examCalculator.portion(100, 10)

# ca.addition(10, 20)
# ca.subtraction(20, 10)
# ca.multiplication(10, 10)
# ca.division(100, 10)
# ca.rest(100, 30)
# ca.portion(100, 10)


#-----------------------------------##
#-----------------------------------##

from examCalculator import addition

addition(10, 20)
#덧셈: 30

subtraction(20, 10)
#NameError: name 'subtraction' is not defined
# (from 모듈명 import (특정)함수명)

# from 모듈명 import '.'
# 특정 함수가 아닌, 모든 함수를 사용하기 위함
# But, 'from 모듈명 import .' 보다는
# 'import examCalculator as ca'를 더 많이 사용함

