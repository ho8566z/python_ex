import urllib.request
import datetime
import json
import essential as es

es.client_id
es.client_secret

# NAVER에서 데이터를 가져오는 역할함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret', client_secret)

    #네이버 서버와 내가 만든 소프트웨어의 호환문제가 발생할 수 있기 때문에 예외처리
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f'[{datetime.datetime.now()}] URL REQUEST SUCCESS')
            # print(f'response data: {response.read().decode('utf-8')}')
            #decode: 바이트(byte) 코드를 문자열(string)로 변환하는 것
            return response.read().decode('utf-8')
    except Exception as e:
        print(f'[{datetime.datetime.now()}] Error: {e}')
        return None
    

# NAVER에서 데이터 검색하는 역할함수
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'   #=>news.json
    parameters = f'?query={urllib.parse.quote(srcText)}&start={start}&display={display}'
    #파라미터(parameters): '?'을 기준으로 앞은 '도메인', 뒤는 '파라미터'

    url = base + node + parameters
    responseDecode = getRequestUrl(url)
    
    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)


def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']
    pDate = datetime.datetime.strptime(post['pubDate'],  '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({
        'cnt': cnt,
        'title': title,
        'description': description,
        'org_link': org_link,
        'link': link,
        'pData': pDate
    })


def main():
    node = 'news'   #'크롤링'하는 대상을 지정
    srcText = input('검색어 입력: ')
    cnt = 0
    jsonResult = [] #json: 데이터 교환형식(프로그램끼리 데이터를 주고 받기 쉽게 만든 텍스트 형식)

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    # print(f'jsonResponse: {jsonResponse}')
    # print(f'jsonResponse total: {jsonResponse['total']}')       #jsonResponse total: 3783987
    # print(f'jsonResponse items 0: {jsonResponse['items'][0]}')
    # print(f'jsonResponse items 0 title: {jsonResponse['items'][0]['title']}')
    # print(f'jsonResponse items 0 description: {jsonResponse['items'][0]['description']}')

    while jsonResponse != None and jsonResponse['display'] != 0:
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        jsonResponse = getNaverSearch(node, srcText, jsonResponse['start'] + jsonResponse['display'], 100)

    #파일로 저장(날씨_naver_news.json)
    with open(f'{srcText}_naver_{node}. json', 'w', encoding='utf8') as f:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True,  ensure_ascii=False)
        f.write(jsonFile)


if __name__ == '__main__':
    main()

