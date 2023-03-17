### JOB SCRAPPER
# 5.3 Initial Request
# https://weworkremotely.com 를 스크래핑 할 것이다 .
"""
1. python을 이용해 이 웹사이트에 들어와야 하고. (get방식 /requests사용 )

2. 모든 li를 찾아야한다 . 그 항목은 ul에 있고,
3. 그건 class가 'jobs'라는 항목 안에 전부 들어있다.

"""
# f를 써야한다. 문자열 안에 변수를 넣기 위해서, 이렇게 해준 결과 base_url과 search_term이 하나의 문자열이
# 될 수 있다.
# https://weworkremotely.com/remote-jobs/search?term=python
from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website.")
else:
    print(response.text)


