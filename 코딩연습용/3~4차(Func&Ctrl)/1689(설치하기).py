# 코드를 실행하기 위해 requests 를 설치한다.
# 설치 방법 및 사용 방법은 https://pypi.org/project/requests/ 문서 참고
# 무작위 유저 정보를 얻어오기 위한 경로 open API https://jsonplaceholder.typicode.com/guide/ 문서 참고
# 반복문을 사용하여 1부터 10까지 총 10명의 데이터를 요청한다.
# 응답 받은 결과에서 사용자의 name과 lat, lng, company name을 하나의 dict로 구성하여 dummy_data 리스트에 삽입하시오.
# 이때, 리스트에 추가는 dummy_data.append(name) 형식으로 진행한다.
# 단, lat(위도)과 lng(경도)는 각각 80 미만, -80 초과인 경우만 삽입한다.
# dummy_data 를 출력한다.


import requests

