import urllib.request
import datetime
import json

SERVICE_KEY = '1fac12c20ae2a975376bc2dedd43773c22483d8f7be8953e009f33d65a5efb06'

def getRequestURL(url):
    req = urllib.request.Request(url)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:    
            print(f'[{datetime.datetime.now()}]: REQUEST COMMUNICATION SUCCESS')
            return res.read().decode('utf-8')

    except Exception as e:
        print(f'[{datetime.datetime.now()}]: REQUEST COMMUNICATION FAIL')
        print(f'e: {e}')
        return None


def getTourismStatesItem(yyyymm, nat_cd, ed_cd):
    serviceURL = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    paraneters = "?"
    paraneters += "_type=json&"
    paraneters += "YM=" + yyyymm + '&'
    paraneters += "NAT_CD=" + nat_cd + '&'
    paraneters += "ED_CD=" + ed_cd + '&'
    paraneters += "serviceKey=" + SERVICE_KEY

    url = serviceURL + paraneters
    res = getRequestURL(url)        #None or not None
    if res == None:
        return None
    else:
        return json.loads(res)
        #json.loads()는 JSON 형식의 문자열(str)을 파이썬 애플리케이션에서 쉽게 사용할 수 있도록 변환함
        #JSON 형식의 문자열(str) --> dic 객체


def getTourismStateService(nat_cd, ed_cd, nStartYear, nEndYear):

    jsonResult = []
    result = []
    natName = ''
    isDataEnd = 0
    dataEND = f'{str(nEndYear)}{str(12)}'
    
    for year in range(nStartYear, nEndYear +1):     #년
        for month in range(1, 13):                  #월
            if isDataEnd == 1:
                break

            yyyymm = f'{str(year)}{str(month):0>2}'      #202010
            jsonData = getTourismStatesItem(yyyymm, nat_cd, ed_cd)
            if jsonData['response']['header']['resultMsg'] == 'OK':

                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1   #데이터 끝 확인용 flag변수
                    dataEND = f'{str(year)}{str(month -1):0>2}'
                    print('DATA END')
                    break

                #json data 확인
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '')  #중  국 -> 중국
                num = jsonData['response']['body']['items']['item']['num']  #방문한 사람 수
                ed = jsonData['response']['body']['items']['item']['ed']    #방한외래관광객

                jsonResult.append({
                    'nat_Name': natName,
                    'nat_cd': nat_cd,
                    'yyyymm': yyyymm,
                    'visit_cnt': num,
                })
    return (jsonResult, natName, ed, dataEND)


def main():

    jsonResult = []
    natName = ''

    print('==================================================')
    print('============국내 입국한 외국인 통계 데이터============')
    print('==================================================')

    nat_cd = input('국가 코드 입력[중국(112), 일본(130), 미국(275)] :  ')
    nStartYear = int(input('데이터 수집 시작 년도 :  '))
    nEndYear = int(input('데이터 수집 끝 년도 :  '))
    ed_cd = 'E' # E: 입국, D: 출국

    jsonResult, natName, ed, dataEND = getTourismStateService(nat_cd, ed_cd, nStartYear, nEndYear)
    # print(f'jsonResult: {jsonResult}')
    # print(f'natName: {natName}')
    # print(f'ed: {ed}')
    # print(f'dateEND: {dataEND}')
    # # jsonResult: 
    # # [
    # # {'nat_Name': '일본', 'nat_cd': '130', 'yyyymm': '202601', 'visit_cnt': 225351}, 
    # # {'nat_Name': '일본', 'nat_cd': '130', 'yyyymm': '202602', 'visit_cnt': 232835}, 
    # # {'nat_Name': '일본', 'nat_cd': '130', 'yyyymm': '202603', 'visit_cnt': 481789}, 
    # # {'nat_Name': '일본', 'nat_cd': '130', 'yyyymm': '202604', 'visit_cnt': 304053}
    # # ]
    # # natName: 일본
    # # ed: 방한외래관광객
    # # dateEND: 202604

    if natName == '':
        print('데이터 수집 오류')
    else:
        print('데이터 수집 성공')
        with open(f'./{natName}_{ed}_{nStartYear}_{dataEND}.json', 'w', encoding='utf-8') as f:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            f.write(jsonFile)


if __name__ == '__main__':
    main()