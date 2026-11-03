var1 = 100
# var2 에는 var1 의 값이 복사되므로 이후 var1 을 바꿔도 var2 는 그대로다
var2 = var1

print(var1)
print(var2)

var1 = 200

print(var1)
print(var2)


num1 = 111
num2 = 222

print(num1)
print(num2)

# temp 에 num1 을 잠시 보관한 뒤 num1 과 num2 를 맞바꾼다
temp = num1
num1 = num2
num2 = temp

print(num1)
print(num2)