# # quiz - 단위환산 프로그램
# '''
# mm 단위의 길이를 입력하면, cm, m, inch, ft 등으로 단위가 변환되어 출력되는 함수가 포함된
# 프로그램을 만들자
# '''

# def convertUnit(lenMm):

#     unitDic = {}

#     unitDic['cm'] = lenMm * .1
#     unitDic['m'] = lenMm * .001
#     unitDic['inch'] = lenMm * .03937
#     unitDic['ft'] = lenMm * .003281

#     return unitDic

# def printLength(lengths):
#     for len in lengths.keys():
#         print(f'{len}: {lengths[len]}{len}')


# inputMmData = int(input('길이(mm) 입력하세요. '))
# resultData = convertUnit(inputMmData)
# printLength(resultData)
# # 길이(mm) 입력하세요. 999
# # cm: 99.9cm
# # m: 0.999m
# # inch: 39.33063inch
# # ft: 3.2777190000000003ft



# # quiz - 할인된 상품 가격표 출력 프로그램
# '''
# DW마트는 고객감사의 일환으로 '오늘의 할인' 이벤트를 진행할 계획입니다.
# 아래의 상품 가격표를 참고해서 '오늘의 할인'을 입력하면 할인된 가격이 출력되는
# 프로그램은 만들자

# 쌀: 9,900
# 상추: 1,900
# 고추: 2,900
# 마늘: 8,900
# 통닭: 5,600
# 햄: 6,900
# 치즈: 3,900
# '''

# standardPrice = {
#     '쌀': 9900,
#     '상추': 1900,
#     '고추': 2900,
#     '마늘': 8900,
#     '통닭': 5600,
#     '햄': 6900,
#     '치즈': 3900
# }

# def getDiscountPrice(rate):
#     dcPrice = {}

#     for goodsName in standardPrice.keys():
#         disPrice = int(standardPrice[goodsName] * (1 - (rate / 100)))
#         dcPrice[goodsName] = disPrice

#     return dcPrice

# def printPrice(priceList):
#     for goodsName, goodsPrice in priceList.items():
#         print(f'{goodsName}\t: {standardPrice[goodsName]}원 -{inputRateData}%(DC)--> {goodsPrice}원')

# inputRateData = int(input('오늘의 할인율 입력: '))

# discountPrice = getDiscountPrice(inputRateData)

# printPrice(discountPrice)
# # 오늘의 할인율 입력: 50
# # 쌀      : 9900원 -50% DC--> 4950원
# # 상추    : 1900원 -50% DC--> 950원
# # 고추    : 2900원 -50% DC--> 1450원
# # 마늘    : 8900원 -50% DC--> 4450원
# # 치즈    : 3900원 -50% DC--> 1950원



# # quiz - 영어 사전

# englishDictionary = {
#     'apple': '사과',
#     'chair': '의자',
#     'doll': '인형',
#     'book': '책',
#     'piano': '피아노',
#     'clock': '시계'
# }

# def printWord(engWord):
#     print(f'{engWord}: {englishDictionary[engWord]}')

# printWord(input('찾고자 하는 영단어 입력: '))
# # 찾고자 하는 영단어 입력: apple
# # 사과



# 모듈이란?
# 프로그램을 개발할 때, 이미 만들어져 있는 기능을 가져다 쓸 수 있는 기능
# 특정 기능(함수)을 포함하고 있는 파일(xxx.py)로 다른 프로그램에 이식해서 사용하는 것

# 모듈의 장점: 프로그램 개발시간 단축, 검증된 코드로서 오류가 적음,
# 기능 구현을 분업화하고 공유할 수 있어 전체적인 작업속도를 향상시킴
# But, 위의 모듈의 장점은 단점이 될 수도 있기에 주의가 필요함

