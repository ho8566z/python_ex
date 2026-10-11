no7 = "cristianoRonaldo"
no10 = "lionelMessi"
no13 = "jisungPark"
print(no7)
print(no10)
print(no13)
print("-------------------------")

# 튜플 언패킹으로 세 변수의 값을 임시 변수 없이 한 번에 돌려 바꾼다
no7, no10, no13 = no10, no13, no7
print(no7)
print(no10)
print(no13)
print("-------------------------")

# 같은 방식으로 한 번 더 돌려 바꾼다
no7, no10, no13 = no10, no13, no7
print(no7)
print(no10)
print(no13)
print("-------------------------")
