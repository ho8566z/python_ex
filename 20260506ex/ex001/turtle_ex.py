# turtle 모듈로 거북이가 움직이며 정삼각형을 그린다.
import turtle

t = turtle.Turtle()
t.shape('turtle')

# 정삼각형의 바깥각은 120도이다.
angle = 120

t.right(angle)
t.forward(100)

t.left(angle)
t.forward(100)

t.left(angle)
t.forward(100)
