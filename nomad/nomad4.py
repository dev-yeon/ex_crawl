# Data structures
"""
print("4.Data structures : 데이터 구조 ----------------------------")
print("4.0 Methods :  data에 연결 - 결합된 데이터의 구조. ")

print(" Python 에는, 3가지의 자료 구조가 있다. "
      "1 번째는 list."
      "2 번째는 tuple"
      "3 번째는 dictionary 이다. ")
print("list= [] 대괄호")
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"
# 이는 단지 variable의 연속이지,  list의 형태는 아니다. list는 한 개의 variable 안에 모든 데이터를 넣을 수 있어야 한다.


days_of_week =  "Mon, Tue, Wed, Thu, Fri"
# print(days_of_week)
days_of_week =["Mon", "Tue", "Wed", "Thu", "Fri"] #print(days_of_week)
name = "nico"
print(name.upper())
print(name.capitalize())
print(name.startswith("n"))
print(name.replace("o","✨"))
print("nico".endswith("o"))
"""

# tuples는 생성한 이후 에는 바꿀 수 없다.
# tuples 을 만들 때는, 소괄호를 써야 하고, 그 안에 아이템에 접근할 때는 대괄호 [ ] 를 써야 한다 ..
# tuple도 인덱스 0.1.2 부터 시작한다.
"""
print("4.2 Tuples ( ) 소괄호  ")
days = ("Mon", "Tue", "Wed")
print(days[0])

print(days[-1])
"""

# list도 마찬가지이지만, -1의 데이터를 요청하면 마지막 데이터를 전달해준다.  (-2는 마지막 하나 이전의..)
# 데이터를 수정해야한다면 list로 짜고 . (가변)
# 한번 생성해서, 그 누구도 건드리게 하고 싶지 않다면 tuples로 짤 수 있다 (불변)
"""
print(" 4.3 Dicts { } 중괄호")
#  4.3 Dicts  key 값과 value 값의 pair 이다.
player = {
    'name': 'nico',
    'age': 12,
    'alive': True,
# 'key' : 'value'
    'fav_food': ["🍔","🍕"]
}
print(player.get('age'))
print(player['fav_food'])
player['fav_food'].append("🥨")
print(player.pop('age'))
print(player['fav_food'])
print(player)
"""
"""
# 4.4 Recap
print("nico".endswith("a"))
# 만약 함수가 독립적으로 사용된다면, '함수'라고 하지만 결합된 함수는, '메소드' 라고 부른다.

# list
numbers = [5,3,1,7,8, "True", True, 12]
numbers.append(["🍔","🍕"])
print(numbers)

print(numbers[-1])

# Tuples
numbers_tuples = (1,2,3,4,5, True, "xxxx")
print(numbers_tuples[-1])

player = {
"name": "nico",
"age": 12,
"alive": True,
"fav_food": ("🍔","🍕"),
"friend" : {
    "name": "lynn",
    "fav_food": ["🧇"] # 딕셔너리 안의 또 다른 딕셔너리 . 
    }
}
player['fav_food'] =="🧇"
player.pop("alive") # alive 키를 완전히 삭제하겠다 . 
player['friend']
['fav_food'].append("🌮")
print(player['friend'])
"""

"""

# 4.5 For Loops
print("4.5 . For Loops")

websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com"
    "tiktok.com"
)
# website[0] --> 이런 방식은 시간이 많이 걸린다.

# 리스트가 얼마나 긴지는 신경 쓰고 싶지 않다.
# 파이선에게, list의 각 item을 활용 해서, 자동으로 코드를 실행 하라고 할 방법을 찾아야 한다.
#

for each in websites:
    print("hello") # tuples 안에 4개의 item이 있어서 각각 4번 출력되었다. 
    
# 그렇다면, 현재 처리중인 item이 뭔지 알고싶다면 .
# list 에 어떤 item인지 알고싶다. 사이클의 어디를 실행하는지 알고싶다.

# 현재 실행중인 item에 접근하는 변수의 이름은 사용자가 마음대로 정할 수 있다. 
for website in websites:
    print("website is equal to", website)
"""

"""
print("4.6 URL Formating ")
websites = (
    "https://google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)
for website in websites:
    if not website.startswith("https://"):
        # websites의 변수 업데이트
        website = f"https://{website}"
    print(website)
"""

#"""
# 4.7 Requests
print("4.7 Requests")
# pypi : 다른 사람들이 만든 파이선 project, modules 를 모아둔 사이트
# https://pypi.org/
# https://pypi.org/project/requests/#description
# requests => 나의 python 코드에서, 웹사이트로 request 보내는 것을 할 수 있게 해준다.

#"""

"""
print("4.8 Status Codes ")
from requests import get
websites = (
    "https://google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)
results = {}
for website in websites:
    if not website.startswith("https://"):
        # websites 의 변수 업데이트
        website = f"https://{website}"
    response = get(website)
   # print(response) # <Response [200]>
   # print(response.status_code) # 200  응답이 200이면 요청에 대한 대답을 받았단 뜻.

    if response.status_code == 200:
        results[website] = "OK"
        # 200 응답을 받는다면, results dictionary 안에 새로운 entry를 추가한다.
    else:
        results[website] = "FAILED"
print(results)
# <Response [200]> 의 뜻은 무엇일까?
# HTTP 상태 코드 200 =웹사이트가 성공적으로 응답하였다.
# HTTP 개요
# https://developer.mozilla.org/ko/docs/Web/HTTP/Overview
# HTTP 상태 코드
# https://developer.mozilla.org/ko/docs/Web/HTTP/Status
"""

#"""
# 4.9  Recap
print("4.9. Recap")

from requests import get
websites = [
    "google.com",
    "https://httpstat.us/502",
    "https://httpstat.us/404",
    "https://httpstat.us/300",
    "https://httpstat.us/200",
    "https://httpstat.us/101",
]
# https://httpstat.us/xxx is service for generating HTTP codes
results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    code = get(website).status_code
    if code >= 500:
        results[website] = "5xx/ server error"
    elif code >= 400:
        results[website] = "4xx/ client error"
    elif code >= 300:
        results[website] = "3xx/ redirection"
    elif code >= 200:
        results[website] = "2xx/ successful"
    elif code >= 100:
        results[website] = "1xx/ informational response"
print(results)
#"""