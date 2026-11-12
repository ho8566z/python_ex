import turtle

t = turtle.Turtle()
t.shape('turtle')

# 입력한 각도만큼 돌고 입력한 길이만큼 가는 동작을 6번 반복해 도형을 그린다
angle = int(input('회전 각도를 입력하세요.'))
length = int(input('전진 길이를 입력하세요.'))
t.speed(1)

t.left(angle)
t.forward(length)

t.left(angle)
t.forward(length)

t.left(angle)
t.forward(length)

t.left(angle)
t.forward(length)

t.left(angle)
t.forward(length)

t.left(angle)
t.forward(length)