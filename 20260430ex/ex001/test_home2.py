red = "maxVerstappen"
fer = "lewisHamilton"
mer = "georgeRussell"

print(red)
print(fer)
print(mer)

print(red + fer)
print(red + " " + fer)

print("___its_all_clear___")

# tes 를 임시 변수로 써서 red 와 fer 의 값을 맞바꾼다
tes = red
red = fer
fer = tes

print(red)
print(fer)

print("___its_all_clear_2___")

red = "maxVerstappen"
fer = "lewisHamilton"
mer = "georgeRussell"

# 임시 변수 하나로 red -> fer -> mer -> red 순서로 값을 한 칸씩 돌린다
tes2 = red
red = fer
fer = mer
mer = tes2

print(red)
print(fer)
print(mer)
