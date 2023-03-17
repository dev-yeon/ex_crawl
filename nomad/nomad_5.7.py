
# 5.7 Job Extraction : Beautiful Soup 의 새로운 내장 기능에 대해 알아보기

from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website.")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')  # list 안의 모든 anchor 을 찾되,
            anchor = anchors[1] # 회사의 로고는 필요 없다.
            # beautiful soup의 좋은점 1:  html 태그 들이 dictionary 처럼 바뀐다.  파이선 dictionary 처럼 쓸 수 있다 .
            link = anchor['href']  # anchor 안의 span 에 접근 하고 싶다.  회사 이름. 직업 이름, 상근직 원격직, 위치
            company, kind, region = anchor.find_all('span', class_="company")

            title = anchor.find('span', class_='title')
            print(company, kind, region, title)
            print("/////////////")
            print("/////////////")


"""
# 모든 html 태그를 beautiful soup entity 로 만드는 기능이 있다.
# class 가 jobs 인 section 을 찾을 때, 이것 들을 string 로 받을 수 있었 지만 그렇게 하지 않았다.

"""
"""
# python 에서, object 의 list 를 가지고 있고, list 의 길이를 안다면,
# list 에서  objects 를 가져 오는 쉬운 코드가 있다.
list_of_numbers = [1, 2, 3]

first, second, third = list_of_numbers
print(first, second, third)
# 하지만, 오직 이 방법은 list 의 길이를 안다는 가정 하에만 쓸 수 있다.
"""
