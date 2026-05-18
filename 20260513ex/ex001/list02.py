# 리스트 데이터 정렬
'''
sort() 함수는 리스트의 아이템을 정렬하는 데 사용한다
reserve 옵션이 False면 오름차순(ASC), True면 내림차순(DESC)으로 정렬한다
'''
# numbers = [5, 3, 7, 1, 6, 9]
# print(f'numbers: {numbers}')        #numbers: [5, 3, 7, 1, 6, 9]

# # 오름차순(ASC)
# numbers.sort()
# print(f'numbers: {numbers}')        #numbers: [1, 3, 5, 6, 7, 9]
# # (=)오름차순
# numbers.sort(reverse=False)
# print(f'numbers: {numbers}')        #numbers: [1, 3, 5, 6, 7, 9]

# # 내림차순(DESC)
# numbers.sort(reverse=True)
# print(f'numbers: {numbers}')        #numbers: [9, 7, 6, 5, 3, 1]


# # 한글 버전
# kor = ['ㄱ', 'ㅇ', 'ㅎ', 'ㅁ', 'ㅌ', 'ㅅ']
# kor.sort()
# print(f'kor: {kor}')                #kor: ['ㄱ', 'ㅁ', 'ㅅ', 'ㅇ', 'ㅌ', 'ㅎ']
# kor.sort(reverse=True)
# print(f'kor: {kor}')                #kor: ['ㅎ', 'ㅌ', 'ㅇ', 'ㅅ', 'ㅁ', 'ㄱ']


# scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
# print(f'scores: {scores}')
# #scores: [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
# scores.sort()
# print(f'scores: {scores}')
# #scores: [70, 75, 75, 78, 80, 84, 85, 88, 90, 90, 92, 92, 95, 95, 100, 100, 100]
# scores.sort(reverse=True)
# print(f'scores: {scores}')
# #scores: [100, 100, 100, 95, 95, 92, 92, 90, 90, 88, 85, 84, 80, 78, 75, 75, 70]


# # quiz) 회의 참석자 정렬하기
# # 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# # names = ['홍길동', '김길동', '이길동', '박길동', '정길동']

# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# names.sort()
# print(f'names: {names}')    #names: ['김길동', '박길동', '이길동', '정길동', '홍길동']
# names.sort(reverse=True)
# print(f'names: {names}')    #names: ['홍길동', '정길동', '이길동', '박길동', '김길동']



# # 리스트 데이터 순서 뒤집기
# # reverse() 함수를 이용하면 리스트의 아이템을 역순으로 뒤집을 수 있다
# vegetables = ['당근', '오이', '양파', '감자', '고구마']
# vegetables.reverse()
# print(f'vegetables: {vegetables}')
# #vegetables: ['고구마', '감자', '양파', '오이', '당근']



# # 리스트 슬라이싱
# # 슬라이싱이란, 리스트에서 필요한 부분의 아이템만 뽑아내는 것을 말한다
# animals = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'animals: {animals}')    #animals: ['호랑이', '사자', '곰', '여우', '늑대']
# '''
#           |1---------------3|
# ['호랑이', '사자', '곰', '여우', '늑대']
# '''
# print(f'animals: {animals[1:4]}')       #[1:4] = 1에서 부터 3까지
# #animals: ['사자', '곰', '여우']
# print(f'animals: {animals}')
# #animals: ['호랑이', '사자', '곰', '여우', '늑대']

# sliceanimals = animals[1:4]
# print(f'sliceanimals: {sliceanimals}')
# #sliceanimals: ['사자', '곰', '여우']

#[n:m] : n 인덱스부터 (m-1) 인덱스 까지의 아이템을 슬라이싱(추출)한다

# animals = ['호랑이', '사자', '곰', '여우', '늑대']
# print(f'animals: {animals[:2]}')    #[:2] : 0(생략)부터 2(2-1)까지 아이템 슬라이싱
# #animals: ['호랑이', '사자']

# print(f'animals: {animals[3:]}')    #[3:] : 3부터 4(생략)까지 아이템 슬라이싱
# #animals: ['여우', '늑대']


# # 뒤에서 2개의 아이템을 슬라이싱
# print(f'animals: {animals[len(animals)-2:]}')   
# #[len(animals)-2:] : len() 함수를 사용하여, 끝에서 부터 2개만 슬라이싱
# #animals: ['여우', '늑대']

# print(f'animals: {animals[:-1]}')
# #[:-1] : 0(생략)부터 -1까지(마지막에서 1개 뺀 만큼만) 슬라이싱
# #animals: ['호랑이', '사자', '곰', '여우']

# print(f'animals: {animals[:]}')
# #animals: ['호랑이', '사자', '곰', '여우', '늑대']

# print(f'animals: {animals[::2]}')
# #[::2] : 0과 2, 그리고 4만 슬라이싱(::2는 스텝 / 1개 하고, 1개 띄고 하는 방식으로)
# #animals: ['호랑이', '곰', '늑대']


# # quiz - 다음 리스트를 보고 답해라

# #1 알파벳 리스트를 역순으로 출력
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# alphabet.reverse()
# print(f'alphabet: {alphabet}')
# #alphabet: ['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


# #2 다음 요구사항에 맞게 alphabet 리스트를 슬라이싱해라
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# #인덱스 2부터 5까지의 아이템을 출력하시오.
# print(f'alphabet: {alphabet[2:6]}')
# #alphabet: ['c', 'd', 'e', 'f']

# #인덱스 0부터 4까지의 아이템을 출력하시오.
# print(f'alphabet: {alphabet[:5]}')
# #alphabet: ['a', 'b', 'c', 'd', 'e']

# #인덱스 3부터 7까지의 아이템을 출력하시오.
# print(f'alphabet: {alphabet[3:8]}')
# #alphabet: ['d', 'e', 'f', 'g', 'h']

# #인덱스 5부터 끝까지의 아이템을 출력하시오.
# print(f'alphabet: {alphabet[5:]}')
# #alphabet: ['f', 'g', 'h', 'i', 'j']

# #인덱스 3부터 8까지의 아이템을 출력하시오.
# print(f'alphabet: {alphabet[3:9]}')
# #alphabet: ['d', 'e', 'f', 'g', 'h', 'i']

# # 뒤에서 4개 아이템을 출력해라
# print(f'alphabet: {alphabet[len(alphabet)-4:]}')
# #alphabet: ['g', 'h', 'i', 'j']

# # (=)뒤에서 4개 아이템을 출력해라
# print(f'alphabet: {alphabet[-4:]}')
# #alphabet: ['g', 'h', 'i', 'j']


#            |-10---9----8----7----6----5----4----3----2----1-|
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(f'alphabet: {alphabet[-5:-2]}')
# #alphabet: ['f', 'g', 'h']


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# print(f'alphabet: {alphabet}')
# #lphabet: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# del alphabet[2:7]
# print(f'del alphabet: {alphabet}')
# #del alphabet: ['a', 'b', 'h', 'i', 'j']
